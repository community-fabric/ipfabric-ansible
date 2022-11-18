#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: inventory_info
short_description: Fetch inventory tables from IP Fabric.
description: Fetch inventory tables from IP Fabric.
author:
  - Alex Gittings (@minitriga)
extends_documentation_fragment:
  - ipfabric.ansible.provider
options:
  snapshot_id:
    description: IP Fabric snapshot ID to use by default for database actions. Defaults to C(False).
    type: str
  filter:
    description: Filter to apply to the inventory tables
    type: dict
    default: {}
  columns:
    description: Add columns you would like to return
    type: list
    elements: str
    default: []
  table:
    description: Table to use from inventory
    choices:
      - devices
      - families
      - fans
      - hosts
      - interfaces
      - models
      - modules
      - phones
      - platforms
      - pn
      - sites
      - vendors
    required: True
    type: str
  report:
    description:
      - Return report information when filtering by report.
    type: str
    required: False
  sort:
    description:
        - Sort IP Fabric API response.
    required: False
    type: dict
"""

EXAMPLES = """
- name: Get devices table from latest snapshot
  ipfabric.ansible.inventory_info:
    provider:
      base_url: "https://demo1.eu.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    table: devices

- name: Get devices for a site on specific snapshot and filter by site
  ipfabric.ansible.inventory_info:
    provider:
      base_url: "https://demo1.eu.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    snapshot_id: bbc15e2e-4e75-4c54-9526-b6d8d3f9ff8b
    table: devices
    filter: {"and": [{"siteName": ["eq","MERAKI_SITE"]}]}

- name: Get devices for a site and only return specific columns
  ipfabric.ansible.inventory_info:
    provider:
      base_url: "https://demo1.eu.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    table: devices
    filter: {"and": [{"siteName": ["eq","MERAKI_SITE"]}]}
    columns:
      - hostname
      - family
      - loginIp
"""

RETURN = """
data:
  description: IP Fabric platform table
  elements: dict
  returned: success
  type: list
  sample:
    - devicesCount: 5,
      family: eos,
      id: arista-eos-veos,
      modelsCount: 1,
      platform: veos,
      vendor: arista
    - devicesCount: 6,
      family: ec2,
      id: aws-ec2-nat,
      modelsCount: 1,
      platform: nat,
      vendor: aws
"""

from ansible_collections.ipfabric.ansible.plugins.module_utils.module import (
    AnsibleIPFModule,
)
from ansible.module_utils.basic import AnsibleModule


choices = [
    'devices',
    'families',
    'fans',
    'hosts',
    'interfaces',
    'models',
    'modules',
    'phones',
    'platforms',
    'pn',
    'sites',
    'vendors'
]


def handle_module(ipf):
    table = ipf.module.params['table']
    filter = ipf.module.params['filter']
    columns = ipf.module.params['columns']
    report = ipf.module.params['report']
    sort = ipf.module.params['sort']
    snapshot_id = ipf.module.params['snapshot_id']

    table = getattr(ipf.ipf.inventory, table)

    try:
        data = table.all(filters=filter, columns=columns, sort=sort, reports=report, snapshot_id=snapshot_id)
    except Exception as e:
        ipf.module.fail_json(
            f"Reponse Code: {e.response.json()['code']}. Message: {e.response.json()['message']}. Please check columns and or filters")

    ipf.module.exit_json(changed=False, data=data)


def main():
    argument_spec = AnsibleIPFModule.provider_argument_spec()
    argument_spec.update(
        snapshot_id=dict(
			type="str", 
			required=False
		),
        table=dict(
            type="str",
            required=True,
            choices=choices,
        ),
        filter=dict(
            type="dict",
            required=False,
            default={},
        ),
        columns=dict(
            type="list",
            required=False,
            default=[],
            elements="str"
        ),
        sort=dict(
			type="dict",
			required=False,
			default={}
		),
		report=dict(
			type='str',
			required=False
		)
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    IPFHelper = AnsibleIPFModule(module)

    handle_module(IPFHelper)


if __name__ == "__main__":
    main()
