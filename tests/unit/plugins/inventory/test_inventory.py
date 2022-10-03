from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
import httpx
from unittest.mock import MagicMock
from ansible_collections.ipfabric.ansible.plugins.inventory.inventory import InventoryModule
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.data import InventoryData
from ansible.template import Templar
import json

# @pytest.fixture()
# def inventory():
#     inventory = InventoryModule()
#     inventory._options = {
#         "provider": {
#             "base_url": "https://demo1.ipfabric.io/",
#             "token": "test_token",
#             "verify": True,
#             "snapshot_id": "$last"
#         },
#         "strict": True,
#         "compose": {},
#         "groups": {},
#         "keyed_groups": [],
#     }
#     inventory.inventory = MagicMock()
#     return inventory

@pytest.fixture()
def inventory():
    r = InventoryModule()
    r.inventory = InventoryData()
    r.templar = Templar(loader=DataLoader())
    return r

def test_verify_file_bad_config(inventory):
    assert inventory.verify_file("ipfabric_inventory.yaml") is False

@pytest.fixture()
def payload():
    import os
    return json.loads(open("tests/unit/plugins/inventory/inventory.json").read())

def test_populate_hostvars(inventory, payload, mocker):
    inventory.get_option = mocker.MagicMock()

    inventory._populate(payload)
    host_foo = inventory.inventory.get_host("L64EXR1")
    host_bar = inventory.inventory.get_host("Leaf-201")
    print(dir(inventory.inventory))
    print(inventory.inventory.hosts)

    assert host_foo.vars['vendor'] == 'cisco'
    assert host_bar.vars['model'] == 'N9K-C93240YC-FX2'

# def test_ipfabric_connection(inventory):
#     # pass
#     loader = DataLoader()

#     with pytest.raises(httpx.HTTPStatusError) as error_message:
#         ipf = inventory.get_ipf()
    # print(error_message.value.response)
