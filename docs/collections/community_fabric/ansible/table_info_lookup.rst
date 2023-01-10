
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

.. _ansible_collections.community_fabric.ansible.table_info_lookup:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

community_fabric.ansible.table_info lookup -- Queries and returns IP Fabric information.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This lookup plugin is part of the `community_fabric.ansible collection <https://galaxy.ansible.com/community_fabric/ansible>`_ (version 0.0.1).

    To install it, use: :code:`ansible-galaxy collection install community\_fabric.ansible`.
    You need further requirements to be able to use this lookup plugin,
    see :ref:`Requirements <ansible_collections.community_fabric.ansible.table_info_lookup_requirements>` for details.

    To use it in a playbook, specify: :code:`community_fabric.ansible.table_info`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Queries IP Fabric via its API and returns information.


.. Aliases


.. Requirements

.. _ansible_collections.community_fabric.ansible.table_info_lookup_requirements:

Requirements
------------
The below requirements are needed on the local controller node that executes this lookup.

- ipfabric




.. Terms

Terms
-----

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-_terms"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-_terms:

      .. rst-class:: ansible-option-title

      **Terms**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-_terms" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The IP Fabric technology and table to query.


      .. raw:: html

        </div>





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
        <div class="ansibleOptionAnchor" id="parameter-base_url"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-base_url:

      .. rst-class:: ansible-option-title

      **base_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-base_url" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Url of the IP Fabric API


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: IPF\_URL


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-columns"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-columns:

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

      Return specific columns from IP Fabric API.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filter"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-filter:

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

      Filter applied to the API call to IP Fabric.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ipf_version"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-ipf_version:

      .. rst-class:: ansible-option-title

      **ipf_version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ipf_version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The version of the IP Fabric REST API.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-report"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-report:

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
        <div class="ansibleOptionAnchor" id="parameter-sort"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-sort:

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
        <div class="ansibleOptionAnchor" id="parameter-token"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-token:

      .. rst-class:: ansible-option-title

      **token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP Fabric API token to be able to gather device information.


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: IPF\_TOKEN


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-verify"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__parameter-verify:

      .. rst-class:: ansible-option-title

      **verify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-verify" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allows connection when SSL certificates are not valid. Set to \ :literal:`false`\  when certificated are not trusted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get devices using lookup inventory plugin (IPF_URL and IPF_TOKEN environment variables set)
      ansible.builtin.debug:
        msg: "{{ lookup('ipfabric.ansible.table_info', 'inventory', 'devices') }}"

    - name: Get devices using lookup inventory plugin
      ansible.builtin.debug:
        msg: "{{ lookup('ipfabric.ansible.table_info', 'inventory', 'devices', base_url='https://<url_here>/', token='<token_here>') }}"

    - name: Get sites and sort by name.
      ansible.builtin.debug:
        msg: "{{ lookup('ipfabric.ansible.table_info', 'inventory', 'sites', sort={'order': 'asc', 'column': 'siteName'}) }}"

    - name: Get interfaces filtered by device (if technology is not specified the default is inventory)
      ansible.builtin.debug:
        msg: "{{ lookup('ipfabric.ansible.table_info', 'interfaces', filter={'hostname': ['eq', 'L38AC20']}, sort={'order': 'asc', 'column':'intName'})}}"

    - name: Get interface that match intent verification rule
      ansible.builtin.debug:
        msg: "{{ lookup('ipfabric.ansible.table_info', 'inventory', 'interfaces', filter={'duplex':['color','eq','20']}, report='/inventory/interfaces')}}"





.. Facts


.. Return values

Return Value
------------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-_list"></div>

      .. _ansible_collections.community_fabric.ansible.table_info_lookup__return-_list:

      .. rst-class:: ansible-option-title

      **Return value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-_list" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      list of composed dictionaries with key and value


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Alex Gittings (@minitriga)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/community-fabric/ipfabric-ansible/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/community-fabric/ipfabric-ansible" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

