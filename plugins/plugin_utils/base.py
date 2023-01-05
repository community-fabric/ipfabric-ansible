from __future__ import absolute_import, division, print_function
from ansible.plugins.lookup import LookupBase
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import AnsibleIPFClientError
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import check_sdk
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import table_choices
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import AnsibleIPFError
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import get_client
from ansible.utils.display import Display

__metaclass__ = type

display = Display()


class IPFLookupBase(LookupBase):
    def warn(self, message):
        display.warning(message)

    def debug(self, message):
        display.debug(message)

    def require_ipf_sdk(self):
        return check_sdk()

    def client(self, **kwargs):
        provider = {
            'base_url': kwargs.get('base_url'),
            'version': kwargs.get('api_version'),
            'verify': kwargs.get('verify'),
            'token': kwargs.get('token')
        }

        client, models = get_client(**provider)

        return client

    def table_info(self, client, technology, table, filter, columns, report, sort, snapshot_id):
        if technology not in table_choices.keys():
            raise AnsibleIPFError(f"{technology} not availble, please select from one of the following: {table_choices.keys()}")

        if table not in table_choices[technology]:
            raise AnsibleIPFError(
                f"{table} is not in the {technology} group. Available choices are {table_choices[technology]}")

        if technology == 'inventory':
            from pprint import pformat
            display.vvvv(pformat(dir(client)))
            table = getattr(client.inventory, table)
        else:
            tech = getattr(client.technology, technology)
            table = getattr(tech, table)

        try:
            data = table.all(filters=filter, columns=columns, sort=sort, reports=report, snapshot_id=snapshot_id)
        except Exception as e:
            raise AnsibleIPFError(f"Reponse Code: {e.response.json()['code']}. Message: {e.response.json()['message']}. Please check columns and or filters")

        return data

    def run(self, terms, variables, **kwargs):
        self.require_ipf_sdk()
        self.set_options(var_options=variables, direct=kwargs)
