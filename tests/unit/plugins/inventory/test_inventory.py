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
from ipfabric import IPFClient
import os

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
    return json.loads(open("tests/unit/plugins/inventory/inventory.json").read())


def test_populate_hostvars(inventory, payload, mocker):
    inventory.get_option = mocker.MagicMock()

    inventory._populate(payload)
    host_foo = inventory.inventory.get_host("IOS1")
    host_bar = inventory.inventory.get_host("SRX1")
    print(dir(inventory.inventory))
    print(inventory.inventory.hosts)

    assert host_foo.vars['vendor'] == 'cisco'
    assert host_bar.vars['version'] == '12.1X46-D25.7'


@pytest.mark.parametrize("transform", ["never", "ignore"])
def test_populate_groups_no_sanitization(inventory, mocker, payload, transform):
    def get_option(opt):
        return dict(
            keyed_groups=[dict(key="sitename", prefix="", separator="")]
        ).get(opt)

    inventory.get_option = mocker.MagicMock(side_effect=get_option)
    mocker.patch("ansible.constants.TRANSFORM_INVALID_GROUP_CHARS", transform)

    inventory._populate(
        payload
    )

    assert set(
        ("all", "ungrouped", "1SITE", "SITE:1", "SITE-1")
    ) == set((inventory.inventory.groups.keys()))


@pytest.mark.parametrize("transform", ["always", "silently"])
def test_populate_groups_sanitization(inventory, mocker, payload, transform):
    def get_option(opt):
        return dict(
            keyed_groups=[dict(key="sitename", prefix="", separator="")]
        ).get(opt)

    inventory.get_option = mocker.MagicMock(side_effect=get_option)
    mocker.patch("ansible.constants.TRANSFORM_INVALID_GROUP_CHARS", transform)

    inventory._populate(
        payload
    )

    assert set(
        ("all", "ungrouped", "_SITE", "SITE_1", "SITE_1")
    ) == set((inventory.inventory.groups.keys()))

def test_provider_no_env_variables(inventory, mocker):
    def get_option(opt):
        return dict().get(opt)

    inventory.get_option = mocker.MagicMock()
    with pytest.raises(RuntimeError) as exc:
        IPFClient()

    assert "IP Fabric base_url not provided or IPF_URL not set" in str(exc.value)

    os.environ['IPF_URL'] = "https://demo1.ipfabric.io"

    with pytest.raises(RuntimeError) as exc:
        IPFClient()

    assert "IP Fabric Token or Username/Password not provided." in str(exc.value)

def test_provider_variables(inventory, mocker):
    def get_option(opt):
        return dict(
            provider = dict(
                base_url = "https://demo1.ipfabric.io/",
                token = "test_token"
            )
        ).get(opt)

    inventory.get_option = mocker.MagicMock(side_effect=get_option)

    with pytest.raises(httpx.HTTPStatusError) as exc:
        inventory.get_ipf()

    assert '401 Unauthorized' in str(exc.value)

def test_constructed_groups(inventory, mocker, payload):
    def get_option(opt):
        return dict(
            groups = dict(
                vsrx = "platform == 'vsrx'"
            )
        ).get(opt)


    inventory.get_option = mocker.MagicMock(side_effect=get_option)

    inventory._populate(payload)

    assert set(
        ("all", "ungrouped", "vsrx")
    ) == set((inventory.inventory.groups.keys()))
