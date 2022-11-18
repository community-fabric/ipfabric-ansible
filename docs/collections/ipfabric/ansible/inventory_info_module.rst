
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

.. _ansible_collections.ipfabric.ansible.inventory_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ipfabric.ansible.inventory_info module -- Fetch inventory tables from IP Fabric.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ipfabric.ansible collection <https://galaxy.ansible.com/ipfabric/ansible>`_ (version 0.0.1).

    To install it, use: :code:`ansible-galaxy collection install ipfabric.ansible`.

    To use it in a playbook, specify: :code:`ipfabric.ansible.inventory_info`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Fetch inventory tables from IP Fabric.


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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-columns:

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

      Add columns you would like to return


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filter"></div>

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-filter:

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

      Filter to apply to the inventory tables


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-provider"></div>

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-provider:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-provider/api_version:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-provider/base_url:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-provider/token:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-provider/verify:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-report:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-snapshot_id:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-sort:

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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__parameter-table:

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

      Table to use from inventory


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

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
      ipfabric.ansible.inventory_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        table: devices

    - name: Get devices for a site on specific snapshot and filter by site
      ipfabric.ansible.inventory_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snapshot_id: bbc15e2e-4e75-4c54-9526-b6d8d3f9ff8b
        table: devices
        filter: {"and": [{"siteName": ["eq","MERAKI_SITE"]}]}

    - name: Get devices for a site and only return specific columns
      ipfabric.ansible.inventory_info:
        provider:
          base_url: "https://demo1.eu.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        table: devices
        filter: {"and": [{"siteName": ["eq","MERAKI_SITE"]}]}
        columns:
          - hostname
          - family
          - loginIp




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

      .. _ansible_collections.ipfabric.ansible.inventory_info_module__return-data:

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

      IP Fabric platform table


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`[{"devicesCount": "5,", "family": "eos,", "id": "arista-eos-veos,", "modelsCount": "1,", "platform": "veos,", "vendor": "arista"}, {"devicesCount": "6,", "family": "ec2,", "id": "aws-ec2-nat,", "modelsCount": "1,", "platform": "nat,", "vendor": "aws"}]`


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

