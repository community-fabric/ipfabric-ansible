#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
module: snapshot_info
short_description: Fetch Snapshot information within IP Fabric.
description: Fetch Snapshot information within IP Fabric.
author:
  - Alex Gittings (@minitriga)
extends_documentation_fragment:
  - community_fabric.ansible.provider
options:
  snapshot_id:
    description: IP Fabric snapshot ID to use by default for database actions. Defaults to C(False).
    type: str
'''

EXAMPLES = '''
- name: Get All Snapshots
  community_fabric.ansible.snapshot_info:
    provider:
      base_url: "https://demo1.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"

- name: Get One Snapshot
  community_fabric.ansible.snapshot_info:
    provider:
      base_url: "https://demo1.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    snapshot_id: bbc15e2e-4e75-4c54-9526-b6d8d3f9ff8b
  register: snapshots
'''

RETURN = '''
data:
  description: IP Fabric snapshot information
  elements: dict
  returned: success
  type: list
  sample:
    - count: 61
      end: '2022-01-26T23:07:39.641000+00:00'
      licensed_count: 61
      locked: false
      name: test_daren
      note: 'Site 35 - Baseline, before adding the Azure infrastructure'
      sites:
        - site_id: '2019877'
          uid: 35COLO
        - site_id: '2019883'
          uid: 35HEADOFFICE
        - site_id: '2019888'
          uid: 35PRODUCTION
        - site_id: '2019895'
          uid: 35SALES
        - site_id: '2019900'
          uid: MPLS
      snapshot_id: d323b197-35bb-41e5-9a42-d4de9b38ccaa
      start: '2022-01-26T22:59:15.816000+00:00'
      state: loaded
      status: done
      version: 5.0.2+5
'''

from ansible_collections.community_fabric.ansible.plugins.module_utils.module import AnsibleIPFModule
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = AnsibleIPFModule.provider_argument_spec()
    argument_spec.update(
        snapshot_id=dict(type="str", required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    IPFHelper = AnsibleIPFModule(module)

    snapshot_id = module.params.get('snapshot_id')
    if snapshot_id:
        snapshot_data = IPFHelper.get_snapshot(snapshot_id)
        snapshot_data = snapshot_data.dict()
    else:
        snapshot_data = IPFHelper.get_snapshots_list()

    module.exit_json(changed=False, data=snapshot_data)


if __name__ == "__main__":
    main()
