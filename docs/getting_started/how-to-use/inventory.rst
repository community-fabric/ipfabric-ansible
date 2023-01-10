============
Inventory
============

Here are some quick examples to get up and running with the inventory module.

The inventory plugin documentation can be found :ref:`here<ansible_collections.community_fabric.ansible.inventory_inventory>`.

Using Keyed Groups to group devices per vendor
----------------------------------------------------------------


.. code-block:: yaml

  ---
  plugin: community_fabric.ansible.inventory
  keyed_groups:
    - key: vendor
      prefix: "network_vendor"
      separator: "_"
