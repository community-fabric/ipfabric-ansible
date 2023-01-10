
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

.. _ansible_collections.community_fabric.ansible.snapshot_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

community_fabric.ansible.snapshot module -- Create, Update, Load, Unload or Delete Snapshots within IP Fabric
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `community_fabric.ansible collection <https://galaxy.ansible.com/community_fabric/ansible>`_ (version 0.0.1).

    To install it, use: :code:`ansible-galaxy collection install community\_fabric.ansible`.

    To use it in a playbook, specify: :code:`community_fabric.ansible.snapshot`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, Update, Load, Unload or Delete Snapshots within IP Fabric


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
        <div class="ansibleOptionAnchor" id="parameter-devices"></div>

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-devices:

      .. rst-class:: ansible-option-title

      **devices**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-devices" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of device serial numbers to rediscover


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-provider"></div>

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-provider:

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

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-provider/api_version:

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

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-provider/base_url:

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

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-provider/token:

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

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-provider/verify:

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
        <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-snapshot_id:

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

      IP Fabric snapshot IF to use by default for database actions. Defaults to \ :literal:`False`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-snapshot_name:

      .. rst-class:: ansible-option-title

      **snapshot_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set snapshot name


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snapshot_note"></div>

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-snapshot_note:

      .. rst-class:: ansible-option-title

      **snapshot_note**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snapshot_note" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set snapshot description


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.community_fabric.ansible.snapshot_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of snapshot.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"load"`
      - :ansible-option-choices-entry:`"unload"`
      - :ansible-option-choices-entry:`"lock"`
      - :ansible-option-choices-entry:`"unlock"`
      - :ansible-option-choices-entry:`"clone"`
      - :ansible-option-choices-entry:`"rediscover"`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Start Snapshot
      community_fabric.ansible.snapshot:
        provider:
          base_url: "https://demo1.ipfabric.io/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"

    - name: Delete Snapshot
      community_fabric.ansible.snapshot:
        provider:
          base_url: "https://10.194.50.6/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
        state: absent

    - name: Unload Snapshot
      community_fabric.ansible.snapshot:
        provider:
          base_url: "https://10.194.50.6/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
        state: unload

    - name: Clone Snapshot
      community_fabric.ansible.snapshot:
        provider:
          base_url: "https://10.194.50.6/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
        state: clone

    - name: Clone Snapshot
      community_fabric.ansible.snapshot:
        provider:
          base_url: "https://10.194.50.6/"
          token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
        snaphot_id: 12dd8c61-129c-431a-b98b-4c9211571f89
        devices:
          - 9AMSST2E75V
        state: rediscover




.. Facts


.. Return values


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

