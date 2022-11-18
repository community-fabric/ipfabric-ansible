from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    name: lookup
    short_description: Queries and returns IP Fabric information.
    description: 
        - Queries IP Fabric via its API and returns information.
    author:
        - Alex Gittings (@minitriga)
    options:
        _terms:
            description:
                - The Nautobot object type to query
            required: True
        base_url:
            description:
                - Url of the IP Fabric API
            env:
                - name: IPF_URL
            required: False
            type: str
        token:
            description:
                - IP Fabric API token to be able to gather device information.
            env:
                - name: IPF_TOKEN
            required: False
            type: str
        ipf_version:
            description:
                - The version of the IP Fabric REST API.
            required: False
        verify:
            description:
                - Allows connection when SSL certificates are not valid. Set to C(false) when certificated are not trusted.
            required: False
            type: bool
        filter:
            description:
                - Filter applied to the API call to IP Fabric.
            required: False
            type: dict
        columns:
            description: 
                - Add columns you would like to return.
            required: False
            type: list
        report:
            description:
                - Return report information when filtering by report.
            required: False
            type: str
    requirements: 
        - ipfabric
"""

EXAMPLES = """
- name: Get devices using lookup inventory plugin (IPF_URL and IPF_TOKEN environment variables set)
  ansible.vuiltin.debug:
    msg: "{{ lookup('ipfabric.ansible.inventory', 'devices') }}"

- name: Get devices using lookup inventory plugin
  ansible.builtin.debug:
    msg: "{{ lookup('ipfabric.ansible.inventory', 'devices', base_url='https://<url_here>/', token='<token_here>') }}"

- name: Get sites and sort by name. 
  ansible.builtin.debug:
    msg: "{{ lookup('ipfabric.ansible.inventory', 'sites', sort={'order': 'asc', 'column': 'siteName'}) }}"

- name: Get interfaces filtered by device and sorted by interface
  ansible.builtin.debug:
    msg: "{{ lookup('ipfabric.ansible.inventory', 'interfaces', filter={'hostname': ['eq', 'L38AC20']}, sort={'order': 'asc', 'column':'intName'})}}"

- name: Get interface that match intent verification rule
  ansible.builtin.debug:
    msg: "{{ lookup('ipfabric.ansible.inventory', 'interfaces', filter={'duplex':['color','eq','20']}, report='/inventory/interfaces')}}"

"""

RETURN = """
  _list:
    description:
      - list of composed dictionaries with key and value
    type: list
"""

from pprint import pformat
from ansible.errors import AnsibleLookupError
from ansible.module_utils.six import raise_from
from ansible.utils.display import Display
from ansible.plugins.lookup import LookupBase


try:
    from ipfabric import IPFClient
except ImportError as imp_exc:
    HAS_IPFABRIC = imp_exc
else:
    HAS_IPFABRIC = None

display = Display()


def get_endpoint(ipfabric, term):

    endpoint_map = {
        "devices": ipfabric.inventory.devices,
        "families": ipfabric.inventory.families,
        "fans": ipfabric.inventory.fans,
        "hosts": ipfabric.inventory.hosts,
        "interfaces": ipfabric.inventory.interfaces,
        "models": ipfabric.inventory.models,
        "modules": ipfabric.inventory.modules,
        "phones": ipfabric.inventory.phones,
        "platforms": ipfabric.inventory.platforms,
        "pn": ipfabric.inventory.pn,
        "sites": ipfabric.inventory.sites,
        "vendors": ipfabric.inventory.vendors,
    }

    return endpoint_map[term]


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        self.set_options(var_options=variables, direct=kwargs)

        if HAS_IPFABRIC:
            raise_from(
                AnsibleLookupError(
                    'IPFabric must be installed to use this plugin'),
                HAS_IPFABRIC
            )

        token = kwargs.get('token')
        verify = kwargs.get('verify')
        version = kwargs.get('api_version')
        base_url = kwargs.get('url')
        snapshot_id = kwargs.get('snapshot_id')
        sort = kwargs.get('sort', {})
        filter = kwargs.get('filter', {})
        columns = kwargs.get('columns', [])
        report = kwargs.get('report')

        if len(terms) > 1:
            raise AnsibleLookupError('Please only select one table to return.')

        if not isinstance(columns, list):
            raise AnsibleLookupError('Columns must be a list.')

        if not isinstance(filter, dict):
            raise AnsibleLookupError('filter must be a dictionary.')

        if not isinstance(sort, dict):
            raise AnsibleLookupError('sort must be a dictionary.')

        provider = {
            'base_url': base_url,
            'token': token,
            'api_version': version,
            'verify': verify
        }

        ipf = IPFClient(**provider)

        if not isinstance(terms, list):
            terms = [terms]

        if filter:
            display.v(f'Filter is: {pformat(filter)}')

        results = []

        for term in terms:
            table = get_endpoint(ipf, term)
            table_results = table.all(
                filters=filter, columns=columns, sort=sort, reports=report, snapshot_id=snapshot_id)

            display.vvvv(pformat(table_results))
            for data in table_results:
                results.append(data)

        return results
