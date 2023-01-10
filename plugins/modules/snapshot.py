#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
module: snapshot
short_description: Create, Update, Load, Unload or Delete Snapshots within IP Fabric
description: Create, Update, Load, Unload or Delete Snapshots within IP Fabric
author:
  - Alex Gittings (@minitriga)
extends_documentation_fragment:
  - community_fabric.ansible.provider
options:
  state:
    description:
      - State of snapshot.
    choices: [ present, absent, load, unload, lock, unlock, clone, rediscover ]
    default: present
    type: str
  snapshot_id:
    description: IP Fabric snapshot IF to use by default for database actions. Defaults to C(False).
    type: str
  snapshot_name:
    description: Set snapshot name
    type: str
  snapshot_note:
    description: Set snapshot description
    type: str
  devices:
    description: List of device serial numbers to rediscover
    type: list
    elements: str
'''

EXAMPLES = '''
- name: Start Snapshot
  community_fabric.ansible.snapshot:
    provider:
      base_url: "https://demo1.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"

- name: Delete Snapshot
  community_fabric.ansible.snapshot:
    provider:
      base_url: "https://10.194.50.6/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
    state: absent

- name: Unload Snapshot
  community_fabric.ansible.snapshot:
    provider:
      base_url: "https://10.194.50.6/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
    state: unload

- name: Clone Snapshot
  community_fabric.ansible.snapshot:
    provider:
      base_url: "https://10.194.50.6/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
    state: clone

- name: Clone Snapshot
  community_fabric.ansible.snapshot:
    provider:
      base_url: "https://10.194.50.6/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
    devices:
      - 9AMSST2E75V
    state: rediscover
'''

from ansible_collections.community_fabric.ansible.plugins.module_utils.module import AnsibleIPFModule
from ansible.module_utils.basic import AnsibleModule
import time


class IPFSnapshot(object):

    def __init__(self, module):
        self.rest = AnsibleIPFModule(module)
        self.module = module

    def create(self, state):
        snapshot_id = self.module.params.get('snapshot_id')

        if state == 'present':
            if not snapshot_id:
                resp = self.rest.ipf.post("snapshots")
                if resp.json()['success']:
                    not_found = True
                    while not_found:
                        snapshots = self.rest.ipf._get_snapshots()
                        for k, v in snapshots.items():
                            if v['state'] == 'discovering':
                                self.module.exit_json(
                                    changed=True, msg=f"Running Discovery {k}", data=v)
                                not_found = False
            else:
                name = self.module.params.get('snapshot_name', None)
                note = self.module.params.get('snapshot_note', None)

                data = {}
                if name is not None:
                    data["name"] = name
                if note is not None:
                    data["note"] = note

                resp = self.rest.ipf.patch(f"snapshots/{snapshot_id}", json=data)
                if resp.status_code == 200:
                    self.module.exit_json(changed=True, msg="Snapshot {snapshot_id} updated.", data=resp.json())
                else:
                    self.module.exit_json(changed=False, msg="Something wrong", data=resp.json())
        elif state in ['load', 'unload']:
            mapping = {
                "load": "loaded",
                "unload": "unloaded"
            }
            resp = self.rest.ipf.get(f"snapshots/{snapshot_id}")
            if resp.json()['state'] == mapping[state]:
                self.module.exit_json(changed=False, msg=f"Snapshot {snapshot_id} already {mapping[state]}", data=resp.json())
            elif resp.json()['locked']:
                self.module.exit_json(changed=False, msg=f"Snapshot {snapshot_id} is locked", data=resp.json())

            resp = self.rest.ipf.post(f'snapshots/{snapshot_id}/{state}')

            if resp.status_code == 204:
                self.module.exit_json(
                    changed=True, msg=f"Successfully {mapping[state]} snapshot {snapshot_id}", data={"snapshot_id": snapshot_id})
        elif state in ['lock', 'unlock']:
            mapping_tf = {
                'lock': True,
                'unlock': False
            }
            mapping = {
                'lock': "locked",
                'unlock': "unlocked"
            }
            resp = self.rest.ipf.get(f"snapshots/{snapshot_id}")
            if resp.json()['locked'] == mapping_tf[state]:
                self.module.exit_json(changed=False, msg=f"Snapshot {snapshot_id} already {mapping[state]}", data=resp.json())

            resp = self.rest.ipf.post(f"snapshots/{snapshot_id}/{state}")
            if resp.status_code == 200:
                self.module.exit_json(changed=True, msg=f"Snapshot {snapshot_id} {mapping[state]}", data={'changed': True})
        elif state in ['clone']:
            resp = self.rest.ipf.post(f"snapshots/{snapshot_id}/clone")
            if resp.status_code == 204:
                cloning = True
                new_snapshot_id = ""
                new_snapshot = None
                is_loaded = True
                while cloning:
                    all_snapshots = self.rest.ipf.get_snapshots()
                    for k, v in all_snapshots.items():
                        if not v.loaded and 'clone' in v.name and v.start == all_snapshots[snapshot_id].start:
                            new_snapshot_id = k
                            new_snapshot = v
                            cloning = False

                if new_snapshot.load(self.rest.ipf, timeout=3, retry=25):
                    while is_loaded:
                        time.sleep(2)
                        if self.rest.ipf.inventory.devices.count(snapshot_id=new_snapshot_id) > 0:
                            is_loaded = False
                self.module.exit_json(changed=True, msg=f"Successfully cloned snapshot {snapshot_id}", data={"changed": True, "snapshot_id": new_snapshot_id})
        elif state in ['rediscover']:
            devices = self.module.params.get('devices', [])

            if devices:
                data = {"snList": devices}
            # raise Exception(data)
            resp = self.rest.ipf.post(f"snapshots/{snapshot_id}/devices", json=data)
            # raise Exception(resp.json())

            if resp.status_code == 200:
                snapshot = self.rest.ipf.get_snapshots()[snapshot_id]
                self.module.exit_json(
                    changed=True,
                    msg=f"Rediscovering {len(devices)} devices for {snapshot_id}",
                    data={'changed': True, 'snapshot': snapshot.dict()}
                )

    def delete(self):
        snapshot_id = self.module.params.get('snapshot_id')

        snapshot = self.rest.get_snapshot(snapshot_id)

        if snapshot:
            if snapshot.state != 'discovering':
                resp = self.rest.ipf.delete(
                    f'snapshots/{snapshot.snapshot_id}')
            else:
                columns = [
                    "downloadFile",
                    "isDone",
                    "name",
                    "snapshot",
                    "status",
                    "username",
                    "id"
                ]
                filters = {
                    "snapshot": [
                        "eq",
                        f"{snapshot_id}"
                    ]
                }
                jobs = self.rest.ipf.fetch_all(
                    'tables/jobs', filters=filters, columns=columns, snapshot=False)
                for job in jobs:
                    if job['name'] == 'discoveryNew' and job['status'] == 'running':
                        self.rest.ipf.post(f'jobs/{job["id"]}/stop')

                resp = self.rest.ipf.delete(
                    f'snapshots/{snapshot.snapshot_id}')
            if resp.status_code == 204:
                self.module.exit_json(
                    changed=True, msg=f"Successfully deleted {snapshot_id}")
            raise Exception(resp)
        else:
            self.module.fail_json(msg=f"Failed to find snapshot {snapshot_id}")


def handle_module(module):
    state = module.params.pop("state")
    snapshot = IPFSnapshot(module)
    if state in ['present', 'load', 'unload', 'lock', 'unlock', 'clone', 'rediscover']:
        snapshot.create(state)
    elif state == 'absent':
        snapshot.delete()


def main():
    argument_spec = AnsibleIPFModule.provider_argument_spec()
    argument_spec.update(
        state=dict(
            choices=["present", 'absent', 'load', 'unload', 'lock', 'unlock', 'clone', 'rediscover'], default="present"
        ),
        snapshot_id=dict(type="str", required=False),
        snapshot_name=dict(type="str", required=False),
        snapshot_note=dict(type="str", required=False),
        devices=dict(type="list", required=False, elements="str"),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        # required_one_of=(['snapshot_id']),
        required_if=(
            [
                ("state", "absent", ("snapshot_id",)),
                ("state", "load", ("snapshot_id",)),
                ("state", "unload", ("snapshot_id",)),
                ("state", "lock", ("snapshot_id",)),
                ("state", "unlock", ("snapshot_id",)),
                ("state", "clone", ("snapshot_id",)),
                ("state", "rediscover", ("snapshot_id", "devices")),
            ]
        ),
        supports_check_mode=True
    )

    handle_module(module)


if __name__ == "__main__":
    main()
