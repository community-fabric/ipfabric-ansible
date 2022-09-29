from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: inventory
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
      api_url:
        description: Url of the IP Fabric API
        required: True
        env:
          - name: IPF_URL
      api_version:
        description: The version of the IP Fabric REST API.
        required: False
      validate_certs:
        description:
          - Allows connection when SSL certificates are not valid. Set to C(false) when certificated are not trusted.
        default: True
        type: boolean
      token:
        description:
          - IP Fabric API token to be able to gather device information.
        required: True
        env:
          - name: IPF_TOKEN
"""

EXAMPLES = """
# inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i inventory.yml

plugin: ipfabric.ansible.inventory
"""

import traceback
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.module_utils.basic import missing_required_lib
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


    def add_device_to_groups(self, device, hostname):


    def main(self):
        ipf = IPFClient(self.api_url, token=self.token)
        
        self.fetch_devices(ipf)

        for device in self.devices_list:
          hostname = device['hostname']
          if device["loginIp"]:
            self.inventory.add_host(host=hostname)
            self.inventory.set_variable(
              hostname,
              "ansible_host",
              device["loginIp"]
            )
            if device["family"]:
              self.inventory.set_variable(
                hostname,
                "family",
                device["family"]
              )

          self.add_device_to_groups(device, hostname)
        

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)

        if not HAS_IPFABRIC:
          raise AnsibleError(f'The IP Fabric dynamic inventory plugin requires ipfabric. Error: {missing_required_lib("ipfabric")}')
        self._read_config_data(path=path)
        self.use_cache = cache

        # IPFabric
        self.token = self.get_option("token")
        self.api_url = self.get_option('api_url')
        self.api_version = self.get_option('api_version')
        self.validate_certs = self.get_option("validate_certs")

        self.main()