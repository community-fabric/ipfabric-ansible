from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = '''
options:
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
            - Allows connection when SSL certificates are not valid.
                Set to C(false) when certificated are not trusted.
        default: True
        type: bool
      timeout:
        description:
          - Set HTTP Timeout
        type: int
        default: None
'''
