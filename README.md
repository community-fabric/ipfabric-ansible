[![Documentation Status](https://readthedocs.org/projects/ipfabric-ansible/badge/?version=latest)](https://ipfabric-ansible.readthedocs.io/en/latest/?badge=latest)

# IP Fabric Ansible Collection
This IP Fabric Ansible collection includes of a variety of Ansible content to help automate the management of an IP Fabric instance. This collection is maintained by the IP Fabric Solution Architecture team.

The official documentation can be cound [here](https://ipfabric-ansible.readthedocs.io/en/latest/).

## Ansible version compatibility
Tested with Ansible Core 2.12+ repleases and the current development version of Ansible. Ansible Core versions before 2.11.0 are not supported. 

## Python version compatibility
This collection depends on the IP Fabric SDK for python (ipfabric).

## Included Content
See below for the current collection content:
- `community_fabric.ansible.inventory`

## Installing this collection
You can install the `community_fabric.ansible` collection with the Ansible Galaxy CLI:

```
ansible-galaxy collection install community_fabric.ansible
```

The python module dependencies are not installed by `ansible-galaxy`. They can be installed manually using pip:

```
pip install ipfabric
```

## Using this collection

### Inventory
Here are some quick examples to get up and running with the inventory module.

```yaml
  ---
plugin: community_fabric.ansible.inventory
keyed_groups:
- key: vendor
    prefix: "network_vendor"
    separator: "_"
```

## Contributing to this collection
*TODO*

## Release notes
0.0.1 Beta Release (IP Fabric Inventory)

## Licensing
*TODO*
