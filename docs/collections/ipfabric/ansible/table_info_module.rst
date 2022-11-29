
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.ipfabric.ansible.table_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ipfabric.ansible.table_info module -- Fetch tables from IP Fabric.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ipfabric.ansible collection <https://galaxy.ansible.com/ipfabric/ansible>`_ (version 0.0.1).

    To install it, use: :code:`ansible-galaxy collection install ipfabric.ansible`.

    To use it in a playbook, specify: :code:`ipfabric.ansible.table_info`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Fetch tables from IP Fabric.


.. Aliases


.. Requirements






.. Options

Parameters
----------


.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-columns"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-columns:

      .. rst-class:: ansible-option-title

      **columns**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-columns" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Columns that are to be returned upon successful query.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filter"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-filter:

      .. rst-class:: ansible-option-title

      **filter**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-filter" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter to apply to the table query.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-provider"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-provider:

      .. rst-class:: ansible-option-title

      **provider**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-provider" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information used to connect to IP Fabric via API


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-provider/api_version"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-provider/api_version:

      .. rst-class:: ansible-option-title

      **api_version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-provider/api_version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The version of the IP Fabric REST API.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-provider/base_url"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-provider/base_url:

      .. rst-class:: ansible-option-title

      **base_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-provider/base_url" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Url of the IP Fabric API


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-provider/token"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-provider/token:

      .. rst-class:: ansible-option-title

      **token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-provider/token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      IP Fabric API token to be able to gather device information.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-provider/verify"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-provider/verify:

      .. rst-class:: ansible-option-title

      **verify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-provider/verify" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Allows connection when SSL certificates are not valid. Set to \ :literal:`false`\  when certificated are not trusted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-report"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-report:

      .. rst-class:: ansible-option-title

      **report**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-report" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Return report information when filtering by report.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-snapshot_id:

      .. rst-class:: ansible-option-title

      **snapshot_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP Fabric snapshot ID to use by default for database actions. Defaults to \ :literal:`False`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-sort:

      .. rst-class:: ansible-option-title

      **sort**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sort IP Fabric API response.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-table"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-table" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specific table to return from API.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"arp\_table"`
      - :ansible-option-choices-entry:`"ipv6\_neighbor\_discovery"`
      - :ansible-option-choices-entry:`"mac\_table"`
      - :ansible-option-choices-entry:`"managed\_duplicate\_ip"`
      - :ansible-option-choices-entry:`"managed\_ip\_ipv4"`
      - :ansible-option-choices-entry:`"managed\_ip\_ipv6"`
      - :ansible-option-choices-entry:`"nat\_pools"`
      - :ansible-option-choices-entry:`"nat\_rules"`
      - :ansible-option-choices-entry:`"virtual\_interfaces"`
      - :ansible-option-choices-entry:`"virtual\_machines"`
      - :ansible-option-choices-entry:`"relay\_global\_stats\_received"`
      - :ansible-option-choices-entry:`"relay\_global\_stats\_relayed"`
      - :ansible-option-choices-entry:`"relay\_global\_stats\_sent"`
      - :ansible-option-choices-entry:`"relay\_global\_stats\_summary"`
      - :ansible-option-choices-entry:`"relay\_interfaces"`
      - :ansible-option-choices-entry:`"relay\_interfaces\_stats\_received"`
      - :ansible-option-choices-entry:`"relay\_interfaces\_stats\_relayed"`
      - :ansible-option-choices-entry:`"relay\_interfaces\_stats\_sent"`
      - :ansible-option-choices-entry:`"server\_excluded\_interfaces"`
      - :ansible-option-choices-entry:`"server\_excluded\_ranges"`
      - :ansible-option-choices-entry:`"server\_leases"`
      - :ansible-option-choices-entry:`"server\_pools"`
      - :ansible-option-choices-entry:`"server\_summary"`
      - :ansible-option-choices-entry:`"balancing"`
      - :ansible-option-choices-entry:`"glbp\_forwarders"`
      - :ansible-option-choices-entry:`"group\_members"`
      - :ansible-option-choices-entry:`"group\_state"`
      - :ansible-option-choices-entry:`"stproot\_alignment"`
      - :ansible-option-choices-entry:`"virtual\_gateways"`
      - :ansible-option-choices-entry:`"average\_rates\_data\_bidirectional"`
      - :ansible-option-choices-entry:`"average\_rates\_data\_bidirectional\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_data\_inbound"`
      - :ansible-option-choices-entry:`"average\_rates\_data\_inbound\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_data\_outbound"`
      - :ansible-option-choices-entry:`"average\_rates\_data\_outbound\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_drops\_bidirectional"`
      - :ansible-option-choices-entry:`"average\_rates\_drops\_bidirectional\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_drops\_inbound"`
      - :ansible-option-choices-entry:`"average\_rates\_drops\_inbound\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_drops\_outbound"`
      - :ansible-option-choices-entry:`"average\_rates\_drops\_outbound\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_errors\_bidirectional"`
      - :ansible-option-choices-entry:`"average\_rates\_errors\_bidirectional\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_errors\_inbound"`
      - :ansible-option-choices-entry:`"average\_rates\_errors\_inbound\_per\_device"`
      - :ansible-option-choices-entry:`"average\_rates\_errors\_outbound"`
      - :ansible-option-choices-entry:`"average\_rates\_errors\_outbound\_per\_device"`
      - :ansible-option-choices-entry:`"connectivity\_matrix"`
      - :ansible-option-choices-entry:`"connectivity\_matrix\_unmanaged\_neighbors\_detail"`
      - :ansible-option-choices-entry:`"connectivity\_matrix\_unmanaged\_neighbors\_summary"`
      - :ansible-option-choices-entry:`"counters\_inbound"`
      - :ansible-option-choices-entry:`"counters\_outbound"`
      - :ansible-option-choices-entry:`"current\_rates\_data\_bidirectional"`
      - :ansible-option-choices-entry:`"current\_rates\_data\_inbound"`
      - :ansible-option-choices-entry:`"current\_rates\_data\_outbound"`
      - :ansible-option-choices-entry:`"duplex"`
      - :ansible-option-choices-entry:`"err\_disabled"`
      - :ansible-option-choices-entry:`"mtu"`
      - :ansible-option-choices-entry:`"point\_to\_point\_over\_ethernet"`
      - :ansible-option-choices-entry:`"point\_to\_point\_over\_ethernet\_sessions"`
      - :ansible-option-choices-entry:`"storm\_control\_all"`
      - :ansible-option-choices-entry:`"storm\_control\_broadcast"`
      - :ansible-option-choices-entry:`"storm\_control\_multicast"`
      - :ansible-option-choices-entry:`"storm\_control\_unicast"`
      - :ansible-option-choices-entry:`"switchport"`
      - :ansible-option-choices-entry:`"transceivers"`
      - :ansible-option-choices-entry:`"transceivers\_errors"`
      - :ansible-option-choices-entry:`"transceivers\_statistics"`
      - :ansible-option-choices-entry:`"transceivers\_triggered\_thresholds"`
      - :ansible-option-choices-entry:`"tunnels\_ipv4"`
      - :ansible-option-choices-entry:`"tunnels\_ipv6"`
      - :ansible-option-choices-entry:`"phones"`
      - :ansible-option-choices-entry:`"devices"`
      - :ansible-option-choices-entry:`"families"`
      - :ansible-option-choices-entry:`"fans"`
      - :ansible-option-choices-entry:`"hosts"`
      - :ansible-option-choices-entry:`"interfaces"`
      - :ansible-option-choices-entry:`"models"`
      - :ansible-option-choices-entry:`"modules"`
      - :ansible-option-choices-entry:`"phones"`
      - :ansible-option-choices-entry:`"platforms"`
      - :ansible-option-choices-entry:`"pn"`
      - :ansible-option-choices-entry:`"sites"`
      - :ansible-option-choices-entry:`"vendors"`
      - :ansible-option-choices-entry:`"virtual\_servers"`
      - :ansible-option-choices-entry:`"virtual\_servers\_f5\_partitions"`
      - :ansible-option-choices-entry:`"virtual\_servers\_pool\_members"`
      - :ansible-option-choices-entry:`"virtual\_servers\_pools"`
      - :ansible-option-choices-entry:`"gateway\_redundancy"`
      - :ansible-option-choices-entry:`"networks"`
      - :ansible-option-choices-entry:`"aaa\_accounting"`
      - :ansible-option-choices-entry:`"aaa\_authentication"`
      - :ansible-option-choices-entry:`"aaa\_authorization"`
      - :ansible-option-choices-entry:`"aaa\_lines"`
      - :ansible-option-choices-entry:`"aaa\_password\_strength"`
      - :ansible-option-choices-entry:`"aaa\_servers"`
      - :ansible-option-choices-entry:`"aaa\_users"`
      - :ansible-option-choices-entry:`"cisco\_smart\_licenses\_authorization"`
      - :ansible-option-choices-entry:`"cisco\_smart\_licenses\_registration"`
      - :ansible-option-choices-entry:`"cisco\_smart\_licenses\_reservations"`
      - :ansible-option-choices-entry:`"dns\_resolver\_servers"`
      - :ansible-option-choices-entry:`"dns\_resolver\_settings"`
      - :ansible-option-choices-entry:`"flow\_overview"`
      - :ansible-option-choices-entry:`"license\_summary"`
      - :ansible-option-choices-entry:`"licenses"`
      - :ansible-option-choices-entry:`"licenses\_detail"`
      - :ansible-option-choices-entry:`"logging\_local"`
      - :ansible-option-choices-entry:`"logging\_remote"`
      - :ansible-option-choices-entry:`"logging\_summary"`
      - :ansible-option-choices-entry:`"netflow\_collectors"`
      - :ansible-option-choices-entry:`"netflow\_devices"`
      - :ansible-option-choices-entry:`"netflow\_interfaces"`
      - :ansible-option-choices-entry:`"ntp\_sources"`
      - :ansible-option-choices-entry:`"ntp\_summary"`
      - :ansible-option-choices-entry:`"port\_mirroring"`
      - :ansible-option-choices-entry:`"ptp\_interfaces"`
      - :ansible-option-choices-entry:`"ptp\_local\_clock"`
      - :ansible-option-choices-entry:`"ptp\_masters"`
      - :ansible-option-choices-entry:`"saved\_config\_consistency"`
      - :ansible-option-choices-entry:`"sflow\_collectors"`
      - :ansible-option-choices-entry:`"sflow\_devices"`
      - :ansible-option-choices-entry:`"sflow\_sources"`
      - :ansible-option-choices-entry:`"snmp\_communities"`
      - :ansible-option-choices-entry:`"snmp\_summary"`
      - :ansible-option-choices-entry:`"snmp\_trap\_hosts"`
      - :ansible-option-choices-entry:`"snmp\_users"`
      - :ansible-option-choices-entry:`"telnet\_access"`
      - :ansible-option-choices-entry:`"l2vpn\_circuit\_cross\_connect"`
      - :ansible-option-choices-entry:`"l2vpn\_point\_to\_multipoint"`
      - :ansible-option-choices-entry:`"l2vpn\_point\_to\_point\_vpws"`
      - :ansible-option-choices-entry:`"l2vpn\_pseudowires"`
      - :ansible-option-choices-entry:`"l3vpn\_pe\_routers"`
      - :ansible-option-choices-entry:`"l3vpn\_pe\_routes"`
      - :ansible-option-choices-entry:`"l3vpn\_pe\_vrfs"`
      - :ansible-option-choices-entry:`"l3vpn\_vrf\_targets"`
      - :ansible-option-choices-entry:`"ldp\_interfaces"`
      - :ansible-option-choices-entry:`"ldp\_neighbors"`
      - :ansible-option-choices-entry:`"rsvp\_forwarding"`
      - :ansible-option-choices-entry:`"rsvp\_interfaces"`
      - :ansible-option-choices-entry:`"rsvp\_neighbors"`
      - :ansible-option-choices-entry:`"igmp\_groups"`
      - :ansible-option-choices-entry:`"igmp\_interfaces"`
      - :ansible-option-choices-entry:`"igmp\_snooping\_global\_config"`
      - :ansible-option-choices-entry:`"igmp\_snooping\_groups"`
      - :ansible-option-choices-entry:`"igmp\_snooping\_vlans"`
      - :ansible-option-choices-entry:`"mac\_table"`
      - :ansible-option-choices-entry:`"mroute\_counters"`
      - :ansible-option-choices-entry:`"mroute\_first\_hop\_router"`
      - :ansible-option-choices-entry:`"mroute\_oil\_detail"`
      - :ansible-option-choices-entry:`"mroute\_overview"`
      - :ansible-option-choices-entry:`"mroute\_sources"`
      - :ansible-option-choices-entry:`"mroute\_table"`
      - :ansible-option-choices-entry:`"pim\_neighbors"`
      - :ansible-option-choices-entry:`"rp\_bsr"`
      - :ansible-option-choices-entry:`"rp\_mappings"`
      - :ansible-option-choices-entry:`"rp\_mappings\_groups"`
      - :ansible-option-choices-entry:`"rp\_overview"`
      - :ansible-option-choices-entry:`"neighbors\_all"`
      - :ansible-option-choices-entry:`"neighbors\_endpoints"`
      - :ansible-option-choices-entry:`"neighbors\_unidirectional"`
      - :ansible-option-choices-entry:`"neighbors\_unmanaged"`
      - :ansible-option-choices-entry:`"unidirectional\_link\_detection\_interfaces"`
      - :ansible-option-choices-entry:`"unidirectional\_link\_detection\_neighbors"`
      - :ansible-option-choices-entry:`"cisco\_fex\_interfaces"`
      - :ansible-option-choices-entry:`"cisco\_fex\_modules"`
      - :ansible-option-choices-entry:`"cisco\_vdc\_devices"`
      - :ansible-option-choices-entry:`"cisco\_vss\_chassis"`
      - :ansible-option-choices-entry:`"cisco\_vss\_vsl"`
      - :ansible-option-choices-entry:`"environment\_fans"`
      - :ansible-option-choices-entry:`"environment\_modules"`
      - :ansible-option-choices-entry:`"environment\_power\_supplies"`
      - :ansible-option-choices-entry:`"environment\_power\_supplies\_fans"`
      - :ansible-option-choices-entry:`"juniper\_cluster"`
      - :ansible-option-choices-entry:`"platform\_cisco\_vss"`
      - :ansible-option-choices-entry:`"poe\_devices"`
      - :ansible-option-choices-entry:`"poe\_interfaces"`
      - :ansible-option-choices-entry:`"poe\_modules"`
      - :ansible-option-choices-entry:`"stacks"`
      - :ansible-option-choices-entry:`"stacks\_members"`
      - :ansible-option-choices-entry:`"stacks\_stack\_ports"`
      - :ansible-option-choices-entry:`"inbound\_balancing\_table"`
      - :ansible-option-choices-entry:`"member\_status\_table"`
      - :ansible-option-choices-entry:`"mlag\_cisco\_vpc"`
      - :ansible-option-choices-entry:`"mlag\_pairs"`
      - :ansible-option-choices-entry:`"mlag\_peers"`
      - :ansible-option-choices-entry:`"mlag\_switches"`
      - :ansible-option-choices-entry:`"outbound\_balancing\_table"`
      - :ansible-option-choices-entry:`"marking"`
      - :ansible-option-choices-entry:`"policing"`
      - :ansible-option-choices-entry:`"policy\_maps"`
      - :ansible-option-choices-entry:`"priority\_queuing"`
      - :ansible-option-choices-entry:`"queuing"`
      - :ansible-option-choices-entry:`"random\_drops"`
      - :ansible-option-choices-entry:`"shapping"`
      - :ansible-option-choices-entry:`"bgp\_address\_families"`
      - :ansible-option-choices-entry:`"bgp\_neighbors"`
      - :ansible-option-choices-entry:`"eigrp\_interfaces"`
      - :ansible-option-choices-entry:`"eigrp\_neighbors"`
      - :ansible-option-choices-entry:`"isis\_interfaces"`
      - :ansible-option-choices-entry:`"isis\_neighbors"`
      - :ansible-option-choices-entry:`"ospf\_interfaces"`
      - :ansible-option-choices-entry:`"ospf\_neighbors"`
      - :ansible-option-choices-entry:`"ospfv3\_interfaces"`
      - :ansible-option-choices-entry:`"ospfv3\_neighbors"`
      - :ansible-option-choices-entry:`"path\_lookup\_checks"`
      - :ansible-option-choices-entry:`"rip\_interfaces"`
      - :ansible-option-choices-entry:`"rip\_neighbors"`
      - :ansible-option-choices-entry:`"route\_stability"`
      - :ansible-option-choices-entry:`"routes\_ipv4"`
      - :ansible-option-choices-entry:`"routes\_ipv6"`
      - :ansible-option-choices-entry:`"summary\_protocols"`
      - :ansible-option-choices-entry:`"summary\_protocols\_bgp"`
      - :ansible-option-choices-entry:`"summary\_protocols\_eigrp"`
      - :ansible-option-choices-entry:`"summary\_protocols\_isis"`
      - :ansible-option-choices-entry:`"summary\_protocols\_ospf"`
      - :ansible-option-choices-entry:`"summary\_protocols\_ospfv3"`
      - :ansible-option-choices-entry:`"summary\_protocols\_rip"`
      - :ansible-option-choices-entry:`"vrf\_detail"`
      - :ansible-option-choices-entry:`"vrf\_interfaces"`
      - :ansible-option-choices-entry:`"vrf\_summary"`
      - :ansible-option-choices-entry:`"aci\_dtep"`
      - :ansible-option-choices-entry:`"aci\_endpoints"`
      - :ansible-option-choices-entry:`"aci\_vlan"`
      - :ansible-option-choices-entry:`"aci\_vrf"`
      - :ansible-option-choices-entry:`"apic\_applications"`
      - :ansible-option-choices-entry:`"apic\_bridge\_domains"`
      - :ansible-option-choices-entry:`"apic\_contexts"`
      - :ansible-option-choices-entry:`"apic\_contracts"`
      - :ansible-option-choices-entry:`"apic\_controllers"`
      - :ansible-option-choices-entry:`"apic\_endpoint\_groups"`
      - :ansible-option-choices-entry:`"apic\_endpoint\_groups\_contracts"`
      - :ansible-option-choices-entry:`"vxlan\_interfaces"`
      - :ansible-option-choices-entry:`"vxlan\_peers"`
      - :ansible-option-choices-entry:`"vxlan\_vni"`
      - :ansible-option-choices-entry:`"vxlan\_vtep"`
      - :ansible-option-choices-entry:`"links"`
      - :ansible-option-choices-entry:`"sites"`
      - :ansible-option-choices-entry:`"acl"`
      - :ansible-option-choices-entry:`"acl\_global\_policies"`
      - :ansible-option-choices-entry:`"acl\_interface"`
      - :ansible-option-choices-entry:`"dhcp\_snooping"`
      - :ansible-option-choices-entry:`"dhcp\_snooping\_bindings"`
      - :ansible-option-choices-entry:`"dmvpn"`
      - :ansible-option-choices-entry:`"ipsec\_gateways"`
      - :ansible-option-choices-entry:`"ipsec\_tunnels"`
      - :ansible-option-choices-entry:`"secure\_ports\_devices"`
      - :ansible-option-choices-entry:`"secure\_ports\_interfaces"`
      - :ansible-option-choices-entry:`"secure\_ports\_users"`
      - :ansible-option-choices-entry:`"zone\_firewall\_interfaces"`
      - :ansible-option-choices-entry:`"zone\_firewall\_policies"`
      - :ansible-option-choices-entry:`"bridges"`
      - :ansible-option-choices-entry:`"guards"`
      - :ansible-option-choices-entry:`"inconsistencies"`
      - :ansible-option-choices-entry:`"inconsistencies\_details"`
      - :ansible-option-choices-entry:`"inconsistencies\_multiple\_stp"`
      - :ansible-option-choices-entry:`"inconsistencies\_ports\_multiple\_neighbors"`
      - :ansible-option-choices-entry:`"inconsistencies\_ports\_vlan\_mismatch"`
      - :ansible-option-choices-entry:`"inconsistencies\_stp\_cdp\_ports\_mismatch"`
      - :ansible-option-choices-entry:`"instances"`
      - :ansible-option-choices-entry:`"neighbors"`
      - :ansible-option-choices-entry:`"ports"`
      - :ansible-option-choices-entry:`"stability"`
      - :ansible-option-choices-entry:`"vlans"`
      - :ansible-option-choices-entry:`"device\_detail"`
      - :ansible-option-choices-entry:`"device\_summary"`
      - :ansible-option-choices-entry:`"l3\_gateways"`
      - :ansible-option-choices-entry:`"network\_summary"`
      - :ansible-option-choices-entry:`"site\_summary"`
      - :ansible-option-choices-entry:`"access\_points"`
      - :ansible-option-choices-entry:`"clients"`
      - :ansible-option-choices-entry:`"controllers"`
      - :ansible-option-choices-entry:`"radios\_detail"`
      - :ansible-option-choices-entry:`"radios\_ssid\_summary"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-technology"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__parameter-technology:

      .. rst-class:: ansible-option-title

      **technology**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-technology" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP Fabric technology


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"addressing"`
      - :ansible-option-choices-entry:`"cloud"`
      - :ansible-option-choices-entry:`"dhcp"`
      - :ansible-option-choices-entry:`"fhrp"`
      - :ansible-option-choices-entry:`"interfaces"`
      - :ansible-option-choices-entry:`"ip\_telephony"`
      - :ansible-option-choices-entry:`"inventory"`
      - :ansible-option-choices-entry:`"load\_balancing"`
      - :ansible-option-choices-entry:`"managed\_networks"`
      - :ansible-option-choices-entry:`"management"`
      - :ansible-option-choices-entry:`"mpls"`
      - :ansible-option-choices-entry:`"multicast"`
      - :ansible-option-choices-entry:`"neighbors"`
      - :ansible-option-choices-entry:`"oam"`
      - :ansible-option-choices-entry:`"platforms"`
      - :ansible-option-choices-entry:`"port\_channels"`
      - :ansible-option-choices-entry:`"qos"`
      - :ansible-option-choices-entry:`"routing"`
      - :ansible-option-choices-entry:`"sdn"`
      - :ansible-option-choices-entry:`"sdwan"`
      - :ansible-option-choices-entry:`"security"`
      - :ansible-option-choices-entry:`"stp"`
      - :ansible-option-choices-entry:`"vlans"`
      - :ansible-option-choices-entry:`"wireless"`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get devices table from latest snapshot
      ipfabric.ansible.table_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        technology: inventory
        table: devices

    - name: Get devices for a site on specific snapshot and filter by site
      ipfabric.ansible.table_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snapshot_id: bbc15e2e-4e75-4c54-9526-b6d8d3f9ff8b
        technology: inventory
        table: devices
        filter: {"and": [{"siteName": ["eq","MERAKI_SITE"]}]}

    - name: Get devices for a site and only return specific columns
      ipfabric.ansible.table_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        technology: inventory
        table: devices
        filter: {"and": [{"siteName": ["eq","MERAKI_SITE"]}]}
        columns:
          - hostname
          - family
          - loginIp

    - name: Get Technology Info
      ipfabric.ansible.table_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        technology: routing
        table: ospf_interfaces

    - name: Filter technology table
      ipfabric.ansible.table_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snapshot_id: bbc15e2e-4e75-4c54-9526-b6d8d3f9ff8b
        technology: addressing
        table: arp_table
        filter: {"and": [{"ip": ["eq","10.241.21.2"]}]}

    - name: Filter and select columns on technology table
      ipfabric.ansible.table_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snapshot_id: bbc15e2e-4e75-4c54-9526-b6d8d3f9ff8b
        technology: addressing
        table: arp_table
        columns:
          - hostname
          - intName
          - ip
          - mac
          - vrf
        filter: {"and": [{"ip": ["eq","10.241.21.2"]}]}




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-data"></div>

      .. _ansible_collections.ipfabric.ansible.table_info_module__return-data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-data" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP Fabric table data.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`[{"hostname": "L1R2", "id": 11134421130628, "intName": "Et0/3", "ip": "10.241.21.2", "mac": "0200.0100.0203", "proxy": false, "siteKey": 2448531, "siteName": "LAB01", "sn": "af1ff02", "vendor": null, "vlanId": null, "vrf": ""}, {"hostname": "L1SW\_PTP", "id": 10742431123304, "intName": "mgmt0", "ip": "10.241.21.2", "mac": "0200.0100.0203", "proxy": false, "siteKey": 2448531, "siteName": "LAB01", "sn": "4c4c4c4c", "vendor": "null,", "vlanId": "null,", "vrf": "management"}]`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Alex Gittings (@minitriga)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/community-fabric/ipfabric-ansible/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/community-fabric/ipfabric-ansible" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

