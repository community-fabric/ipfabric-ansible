from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = """
    name: table_info
    short_description: Queries and returns IP Fabric information.
    description:
        - Queries IP Fabric via its API and returns information.
    author:
        - Alex Gittings (@minitriga)
    options:
        _terms:
            description:
                - The IP Fabric technology and table to query.
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
                - Return specific columns from IP Fabric API.
            required: False
            type: list
            elements: str
        sort:
            description:
                - Sort IP Fabric API response.
            required: False
            type: dict
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
  ansible.builtin.debug:
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
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import AnsibleIPFModule
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import table_choices
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import all_tables
from ansible_collections.ipfabric.ansible.plugins.plugin_utils.base import IPFLookupBase


try:
    from ipfabric import IPFClient
except ImportError as imp_exc:
    HAS_IPFABRIC = imp_exc
else:
    HAS_IPFABRIC = None

display = Display()


class LookupModule(IPFLookupBase):

    def run(self, terms, variables=None, **kwargs):
        super().run(terms, variables, **kwargs)

        snapshot_id = kwargs.get('snapshot_id')
        sort = kwargs.get('sort', {})
        filter = kwargs.get('filter', {})
        columns = kwargs.get('columns', [])
        report = kwargs.get('report')

        client = self.client(**kwargs)

        if len(terms) > 2:
            raise AnsibleLookupError('Only two terms are accepted.')

        if not isinstance(columns, list):
            raise AnsibleLookupError('Columns must be a list.')

        if not isinstance(filter, dict):
            raise AnsibleLookupError('filter must be a dictionary.')

        if not isinstance(sort, dict):
            raise AnsibleLookupError('sort must be a dictionary.')

        if not isinstance(terms, list):
            terms = [terms]

        if filter:
            display.v(f'Filter is: {pformat(filter)}')

        results = []

        if len(terms) == 2:
            technology = terms[0]
            table = terms[1]
        elif len(terms) == 1:
            technology = 'inventory'
            table = terms[0]
        else:
            raise AnsibleLookupError("No terms provided.")

        if technology not in table_choices.keys():
            raise AnsibleLookupError(message=f'{technology} not in available choices: {table_choices.keys()}')

        if table not in all_tables:
            raise AnsibleLookupError(message=f'{table} not in available choices: {table_choices[technology]}')

        table_results = self.table_info(client, technology, table, filter, columns, report, sort, snapshot_id)

        for data in table_results:
            results.append(data)

        return results
