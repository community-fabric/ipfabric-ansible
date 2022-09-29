from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: inventory
    extends_documentation_fragment:
      - constructed
    author:
      - Alex Gittings (@minitriga)
    short_description: IP Fabric inventory source
    description:
      - Get inventory hosts from IP Fabric
    extends_document_fragments:
      - constructed
      - inventory_cache
    options:
      plugin:
        description: token that ensures this is a source file for the 'ipfabric' plugin.
        required: True
        choices: ['ipfabric.ansible.inventory']
      provider:
        description: 
          - Information used to connect to IPFabric via API
        type: dict
        required: True
        suboptions:
          base_url:
            description: Url of the IP Fabric API
            required: True
            type: str
            env:
              - name: IPF_URL
          token:
            description:
              - IP Fabric API token to be able to gather device information.
            required: True
            type: str
            env:
              - name: IPF_TOKEN
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
"""

EXAMPLES = """
# inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i inventory.yml

plugin: ipfabric.ansible.inventory
"""

import traceback
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils._text import to_text
from ansible.errors import AnsibleError

IPFABRIC_IMP_ERR = None
try:
  from ipfabric import IPFClient
  HAS_IPFABRIC = True
except ImportError:
  IPFABRIC_IMP_ERR = traceback.format_exc()
  HAS_IPFABRIC = False

class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = "ipfabric.ansible.inventory"

    def fetch_devices(self, ipf):
      self.devices_list = ipf.inventory.devices.all()

    def main(self):
      ipf = IPFClient(**self.get_option('provider'))
      self.fetch_devices(ipf)

      for device in self.devices_list:
        hostname = device['hostname']
        if device["loginIp"] and (device['devType'] != 'ap'):
          new_vars = dict()
          self.inventory.add_host(host=to_text(hostname))
          for devicevar, deviceval in device.items():
            self.inventory.set_variable(to_text(hostname), devicevar.lower(), deviceval)
          new_vars[devicevar.lower()] = deviceval

          strict = self.get_option('strict')
          self._add_host_to_composed_groups(self.get_option('groups'), new_vars, to_text(hostname), strict=strict)
          self._add_host_to_keyed_groups(self.get_option("keyed_groups"), new_vars, to_text(hostname), strict=strict)
        

    def parse(self, inventory, loader, path, cache=True):
      super(InventoryModule, self).parse(inventory, loader, path)

      if not HAS_IPFABRIC:
        raise AnsibleError(f'The IP Fabric dynamic inventory plugin requires ipfabric. Error: {missing_required_lib("ipfabric")}')
      self._read_config_data(path=path)
      self.use_cache = cache

      # IPFabric
      print(self.get_option('provider'))

      self.main()