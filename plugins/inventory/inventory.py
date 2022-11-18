from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: inventory
    author:
      - Alex Gittings (@minitriga)
    short_description: IP Fabric inventory source
    description:
      - Get inventory hosts from IP Fabric
    options:
      plugin:
        description: token that ensures this is a source file for the 'ipfabric' plugin.
        required: True
        choices: ['ipfabric.ansible.inventory']
      provider:
        description:
          - Information used to connect to IP Fabric via API
        type: dict
        required: True
        suboptions:
          base_url:
            description: Url of the IP Fabric API
            required: True
            type: str
          token:
            description:
              - IP Fabric API token to be able to gather device information.
            required: True
            type: str
          api_version:
            description: The version of the IP Fabric REST API.
            type: str
          verify:
            description:
              - Allows connection when SSL certificates are not valid. Set to C(false) when certificated are not trusted.
            default: True
            type: boolean
      snapshot_id:
        description:
          - IP Fabric snapshot IF to use by default for database actions. Defaults to C($last).
        default: "$last"
        type: string
        required: False
      filter:
        description: Filter to apply to the inventory tables
        type: dict
        default: {}
        required: False
      columns:
        description: Add columns you would like to return
        type: list
        elements: str
        default: []
        required: False
    extends_documentation_fragment:
      - inventory_cache
      - constructed
"""

EXAMPLES = """
# inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i inventory.yml

plugin: ipfabric.ansible.inventory
provider:
  base_url: https://demo1.eu.ipfabric.io/
  token: test-token
keyed_groups:
  - key: sitename
    prefix: ""
    separator: ""
groups:
  ciscoios: "family == 'ios'"
filter:
  siteName: ['like', 'L71']
columns:
  - uptime
  - vendor
"""

from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text
from ansible.module_utils.basic import missing_required_lib
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.inventory.group import to_safe_group_name
import traceback
from pprint import pformat

IPFABRIC_IMP_ERR = None
try:
    from ipfabric import IPFClient
    HAS_IPFABRIC = True
except ImportError:
    IPFABRIC_IMP_ERR = traceback.format_exc()
    HAS_IPFABRIC = False


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = "ipfabric.ansible.inventory"

    # Constructable methods use the following function to construct group names. By
    # default, characters that are not valid in python variables, are always replaced by
    # underscores. We are overriding this with a function that respects the
    # TRANSFORM_INVALID_GROUP_CHARS configuration option and allows users to control the
    # behavior.
    _sanitize_group_name = staticmethod(to_safe_group_name)

    def fetch_devices(self, ipf):
        filter = self.get_option('filter')
        columns = self.get_option('columns')

        if columns:
            if 'loginIp' not in columns:
                columns.append('loginIp')
            if 'hostname' not in columns:
                columns.append('hostname')

        self.devices_list = ipf.inventory.devices.all(filters=filter, columns=columns, snapshot_id=self.get_option('snapshot_id'))

    def get_ipf(self):
        return IPFClient(**self.get_option('provider'))

    def _populate(self, records):
        for device in records:
            hostname = device['hostname']
            if device["loginIp"]:
                new_vars = dict()
                self.inventory.add_host(host=to_text(hostname))
                self.inventory.set_variable(to_text(hostname), 'ansible_host', device['loginIp'])
                for devicevar, deviceval in device.items():
                    self.inventory.set_variable(to_text(hostname), devicevar.lower(), deviceval)
                    new_vars[devicevar.lower()] = deviceval

                    strict = self.get_option('strict')

                    self._set_composite_vars(self.get_option('compose'), new_vars, to_text(hostname), strict=strict)
                    self._add_host_to_composed_groups(self.get_option('groups'), new_vars, to_text(hostname), strict=strict)
                    self._add_host_to_keyed_groups(self.get_option("keyed_groups"), new_vars, to_text(hostname), strict=strict)

    def main(self):
        ipf = self.get_ipf()
        self.fetch_devices(ipf)

        self._populate(self.devices_list)

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)

        if not HAS_IPFABRIC:
            raise AnsibleError(f'The IP Fabric dynamic inventory plugin requires ipfabric. Error: {missing_required_lib("ipfabric")}')

        self._read_config_data(path=path)
        self.use_cache = cache

        self.main()
