#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: technology_info
short_description: Fetch technology tables from IP Fabric.
description: Fetch technology tables from IP Fabric.
author:
  - Alex Gittings (@minitriga)
extends_documentation_fragment:
  - ipfabric.ansible.provider
options:
  snapshot_id:
    description: IP Fabric snapshot ID to use by default for database actions. Defaults to C(False).
    type: str
  filter:
    description: Filter to apply to the technology table
    type: dict
    default: {}
  columns:
    description: Add columns you would like to return
    type: list
    elements: str
    default: []
  technology:
    description: IP Fabric technology
    choices:
      - addressing
      - cloud
      - dhcp
      - fhrp
      - interfaces
      - ip_telephony
      - load_balancing
      - managed_networks
      - management
      - mpls
      - multicast
      - neighbors
      - oam
      - platforms
      - port_channels
      - qos
      - routing
      - sdn
      - sdwan
      - security
      - stp
      - vlans
      - wireless
    required: True
    type: str
  table:
    description: Table to use from technology table
    choices:
      - arp_table
      - ipv6_neighbor_discovery
      - mac_table
      - managed_duplicate_ip
      - managed_ip_ipv4
      - managed_ip_ipv6
      - nat_pools
      - nat_rules
      - virtual_interfaces
      - virtual_machines
      - relay_global_stats_received
      - relay_global_stats_relayed
      - relay_global_stats_sent
      - relay_global_stats_summary
      - relay_interfaces
      - relay_interfaces_stats_received
      - relay_interfaces_stats_relayed
      - relay_interfaces_stats_sent
      - server_excluded_interfaces
      - server_excluded_ranges
      - server_leases
      - server_pools
      - server_summary
      - balancing
      - glbp_forwarders
      - group_members
      - group_state
      - stproot_alignment
      - virtual_gateways
      - average_rates_data_bidirectional
      - average_rates_data_bidirectional_per_device
      - average_rates_data_inbound
      - average_rates_data_inbound_per_device
      - average_rates_data_outbound
      - average_rates_data_outbound_per_device
      - average_rates_drops_bidirectional
      - average_rates_drops_bidirectional_per_device
      - average_rates_drops_inbound
      - average_rates_drops_inbound_per_device
      - average_rates_drops_outbound
      - average_rates_drops_outbound_per_device
      - average_rates_errors_bidirectional
      - average_rates_errors_bidirectional_per_device
      - average_rates_errors_inbound
      - average_rates_errors_inbound_per_device
      - average_rates_errors_outbound
      - average_rates_errors_outbound_per_device
      - connectivity_matrix
      - connectivity_matrix_unmanaged_neighbors_detail
      - connectivity_matrix_unmanaged_neighbors_summary
      - counters_inbound
      - counters_outbound
      - current_rates_data_bidirectional
      - current_rates_data_inbound
      - current_rates_data_outbound
      - duplex
      - err_disabled
      - mtu
      - point_to_point_over_ethernet
      - point_to_point_over_ethernet_sessions
      - storm_control_all
      - storm_control_broadcast
      - storm_control_multicast
      - storm_control_unicast
      - switchport
      - transceivers
      - transceivers_errors
      - transceivers_statistics
      - transceivers_triggered_thresholds
      - tunnels_ipv4
      - tunnels_ipv6
      - phones
      - virtual_servers
      - virtual_servers_f5_partitions
      - virtual_servers_pool_members
      - virtual_servers_pools
      - gateway_redundancy
      - networks
      - aaa_accounting
      - aaa_authentication
      - aaa_authorization
      - aaa_lines
      - aaa_password_strength
      - aaa_servers
      - aaa_users
      - cisco_smart_licenses_authorization
      - cisco_smart_licenses_registration
      - cisco_smart_licenses_reservations
      - dns_resolver_servers
      - dns_resolver_settings
      - flow_overview
      - license_summary
      - licenses
      - licenses_detail
      - logging_local
      - logging_remote
      - logging_summary
      - netflow_collectors
      - netflow_devices
      - netflow_interfaces
      - ntp_sources
      - ntp_summary
      - port_mirroring
      - ptp_interfaces
      - ptp_local_clock
      - ptp_masters
      - saved_config_consistency
      - sflow_collectors
      - sflow_devices
      - sflow_sources
      - snmp_communities
      - snmp_summary
      - snmp_trap_hosts
      - snmp_users
      - telnet_access
      - l2vpn_circuit_cross_connect
      - l2vpn_point_to_multipoint
      - l2vpn_point_to_point_vpws
      - l2vpn_pseudowires
      - l3vpn_pe_routers
      - l3vpn_pe_routes
      - l3vpn_pe_vrfs
      - l3vpn_vrf_targets
      - ldp_interfaces
      - ldp_neighbors
      - rsvp_forwarding
      - rsvp_interfaces
      - rsvp_neighbors
      - igmp_groups
      - igmp_interfaces
      - igmp_snooping_global_config
      - igmp_snooping_groups
      - igmp_snooping_vlans
      - mac_table
      - mroute_counters
      - mroute_first_hop_router
      - mroute_oil_detail
      - mroute_overview
      - mroute_sources
      - mroute_table
      - pim_neighbors
      - rp_bsr
      - rp_mappings
      - rp_mappings_groups
      - rp_overview
      - neighbors_all
      - neighbors_endpoints
      - neighbors_unidirectional
      - neighbors_unmanaged
      - unidirectional_link_detection_interfaces
      - unidirectional_link_detection_neighbors
      - cisco_fex_interfaces
      - cisco_fex_modules
      - cisco_vdc_devices
      - cisco_vss_chassis
      - cisco_vss_vsl
      - environment_fans
      - environment_modules
      - environment_power_supplies
      - environment_power_supplies_fans
      - juniper_cluster
      - platform_cisco_vss
      - poe_devices
      - poe_interfaces
      - poe_modules
      - stacks
      - stacks_members
      - stacks_stack_ports
      - inbound_balancing_table
      - member_status_table
      - mlag_cisco_vpc
      - mlag_pairs
      - mlag_peers
      - mlag_switches
      - outbound_balancing_table
      - marking
      - policing
      - policy_maps
      - priority_queuing
      - queuing
      - random_drops
      - shapping
      - bgp_address_families
      - bgp_neighbors
      - eigrp_interfaces
      - eigrp_neighbors
      - isis_interfaces
      - isis_neighbors
      - ospf_interfaces
      - ospf_neighbors
      - ospfv3_interfaces
      - ospfv3_neighbors
      - path_lookup_checks
      - rip_interfaces
      - rip_neighbors
      - route_stability
      - routes_ipv4
      - routes_ipv6
      - summary_protocols
      - summary_protocols_bgp
      - summary_protocols_eigrp
      - summary_protocols_isis
      - summary_protocols_ospf
      - summary_protocols_ospfv3
      - summary_protocols_rip
      - vrf_detail
      - vrf_interfaces
      - vrf_summary
      - aci_dtep
      - aci_endpoints
      - aci_vlan
      - aci_vrf
      - apic_applications
      - apic_bridge_domains
      - apic_contexts
      - apic_contracts
      - apic_controllers
      - apic_endpoint_groups
      - apic_endpoint_groups_contracts
      - vxlan_interfaces
      - vxlan_peers
      - vxlan_vni
      - vxlan_vtep
      - links
      - sites
      - acl
      - acl_global_policies
      - acl_interface
      - dhcp_snooping
      - dhcp_snooping_bindings
      - dmvpn
      - ipsec_gateways
      - ipsec_tunnels
      - secure_ports_devices
      - secure_ports_interfaces
      - secure_ports_users
      - zone_firewall_interfaces
      - zone_firewall_policies
      - bridges
      - guards
      - inconsistencies
      - inconsistencies_details
      - inconsistencies_multiple_stp
      - inconsistencies_ports_multiple_neighbors
      - inconsistencies_ports_vlan_mismatch
      - inconsistencies_stp_cdp_ports_mismatch
      - instances
      - neighbors
      - ports
      - stability
      - vlans
      - device_detail
      - device_summary
      - l3_gateways
      - network_summary
      - site_summary
      - access_points
      - clients
      - controllers
      - radios_detail
      - radios_ssid_summary
    required: True
    type: str
  report:
    description:
      - Return report information when filtering by report.
    type: str
    required: False
  sort:
    description:
        - Sort IP Fabric API response.
    required: False
    type: dict
"""

EXAMPLES = """
- name: Get Technology Info
  ipfabric.ansible.technology_info:
    provider:
      base_url: "https://demo1.eu.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    technology: routing
    table: ospf_interfaces

- name: Filter technology table
  ipfabric.ansible.technology_info:
    provider:
      base_url: "https://demo1.eu.ipfabric.io/"
      token: "{{ lookup('ansible.builtin.env', 'IPF_TOKEN')}}"
    snapshot_id: bbc15e2e-4e75-4c54-9526-b6d8d3f9ff8b
    technology: addressing
    table: arp_table
    filter: {"and": [{"ip": ["eq","10.241.21.2"]}]}

- name: Filter and select columns on technology table
  ipfabric.ansible.technology_info:
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
"""

RETURN = """
data:
  description: IP Fabric technology table
  elements: dict
  returned: success
  type: list
  sample:
    - hostname: L1R2
      id: 11134421130628
      intName: Et0/3
      ip: 10.241.21.2
      mac: 0200.0100.0203
      proxy: false
      siteKey: 2448531
      siteName: LAB01
      sn: af1ff02
      vendor: null
      vlanId: null
      vrf: ""
    - hostname: L1SW_PTP
      id: 10742431123304
      intName: mgmt0
      ip: 10.241.21.2
      mac: 0200.0100.0203
      proxy: false
      siteKey: 2448531
      siteName: LAB01
      sn: 4c4c4c4c
      vendor: null,
      vlanId: null,
      vrf: management
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ipfabric.ansible.plugins.module_utils.module import (
    AnsibleIPFModule,
)

choices = {
    "addressing": [
        "arp_table",
        "ipv6_neighbor_discovery",
        "mac_table",
        "managed_duplicate_ip",
        "managed_ip_ipv4",
        "managed_ip_ipv6",
        "nat_pools",
        "nat_rules",
    ],
    "cloud": ["virtual_interfaces", "virtual_machines"],
    "dhcp": [
        "relay_global_stats_received",
        "relay_global_stats_relayed",
        "relay_global_stats_sent",
        "relay_global_stats_summary",
        "relay_interfaces",
        "relay_interfaces_stats_received",
        "relay_interfaces_stats_relayed",
        "relay_interfaces_stats_sent",
        "server_excluded_interfaces",
        "server_excluded_ranges",
        "server_leases",
        "server_pools",
        "server_summary",
    ],
    "fhrp": [
        "balancing",
        "glbp_forwarders",
        "group_members",
        "group_state",
        "stproot_alignment",
        "virtual_gateways",
    ],
    "interfaces": [
        "average_rates_data_bidirectional",
        "average_rates_data_bidirectional_per_device",
        "average_rates_data_inbound",
        "average_rates_data_inbound_per_device",
        "average_rates_data_outbound",
        "average_rates_data_outbound_per_device",
        "average_rates_drops_bidirectional",
        "average_rates_drops_bidirectional_per_device",
        "average_rates_drops_inbound",
        "average_rates_drops_inbound_per_device",
        "average_rates_drops_outbound",
        "average_rates_drops_outbound_per_device",
        "average_rates_errors_bidirectional",
        "average_rates_errors_bidirectional_per_device",
        "average_rates_errors_inbound",
        "average_rates_errors_inbound_per_device",
        "average_rates_errors_outbound",
        "average_rates_errors_outbound_per_device",
        "connectivity_matrix",
        "connectivity_matrix_unmanaged_neighbors_detail",
        "connectivity_matrix_unmanaged_neighbors_summary",
        "counters_inbound",
        "counters_outbound",
        "current_rates_data_bidirectional",
        "current_rates_data_inbound",
        "current_rates_data_outbound",
        "duplex",
        "err_disabled",
        "mtu",
        "point_to_point_over_ethernet",
        "point_to_point_over_ethernet_sessions",
        "storm_control_all",
        "storm_control_broadcast",
        "storm_control_multicast",
        "storm_control_unicast",
        "switchport",
        "transceivers",
        "transceivers_errors",
        "transceivers_statistics",
        "transceivers_triggered_thresholds",
        "tunnels_ipv4",
        "tunnels_ipv6",
    ],
    "ip_telephony": ["phones"],
    "load_balancing": [
        "virtual_servers",
        "virtual_servers_f5_partitions",
        "virtual_servers_pool_members",
        "virtual_servers_pools",
    ],
    "managed_networks": ["gateway_redundancy", "networks"],
    "management": [
        "aaa_accounting",
        "aaa_authentication",
        "aaa_authorization",
        "aaa_lines",
        "aaa_password_strength",
        "aaa_servers",
        "aaa_users",
        "cisco_smart_licenses_authorization",
        "cisco_smart_licenses_registration",
        "cisco_smart_licenses_reservations",
        "dns_resolver_servers",
        "dns_resolver_settings",
        "flow_overview",
        "license_summary",
        "licenses",
        "licenses_detail",
        "logging_local",
        "logging_remote",
        "logging_summary",
        "netflow_collectors",
        "netflow_devices",
        "netflow_interfaces",
        "ntp_sources",
        "ntp_summary",
        "port_mirroring",
        "ptp_interfaces",
        "ptp_local_clock",
        "ptp_masters",
        "saved_config_consistency",
        "sflow_collectors",
        "sflow_devices",
        "sflow_sources",
        "snmp_communities",
        "snmp_summary",
        "snmp_trap_hosts",
        "snmp_users",
        "telnet_access",
    ],
    "mpls": [
        "l2vpn_circuit_cross_connect",
        "l2vpn_point_to_multipoint",
        "l2vpn_point_to_point_vpws",
        "l2vpn_pseudowires",
        "l3vpn_pe_routers",
        "l3vpn_pe_routes",
        "l3vpn_pe_vrfs",
        "l3vpn_vrf_targets",
        "ldp_interfaces",
        "ldp_neighbors",
        "rsvp_forwarding",
        "rsvp_interfaces",
        "rsvp_neighbors",
    ],
    "multicast": [
        "igmp_groups",
        "igmp_interfaces",
        "igmp_snooping_global_config",
        "igmp_snooping_groups",
        "igmp_snooping_vlans",
        "mac_table",
        "mroute_counters",
        "mroute_first_hop_router",
        "mroute_oil_detail",
        "mroute_overview",
        "mroute_sources",
        "mroute_table",
        "pim_neighbors",
        "rp_bsr",
        "rp_mappings",
        "rp_mappings_groups",
        "rp_overview",
    ],
    "neighbors": [
        "neighbors_all",
        "neighbors_endpoints",
        "neighbors_unidirectional",
        "neighbors_unmanaged",
    ],
    "oam": [
        "unidirectional_link_detection_interfaces",
        "unidirectional_link_detection_neighbors",
    ],
    "platforms": [
        "cisco_fex_interfaces",
        "cisco_fex_modules",
        "cisco_vdc_devices",
        "cisco_vss_chassis",
        "cisco_vss_vsl",
        "environment_fans",
        "environment_modules",
        "environment_power_supplies",
        "environment_power_supplies_fans",
        "juniper_cluster",
        "platform_cisco_vss",
        "poe_devices",
        "poe_interfaces",
        "poe_modules",
        "stacks",
        "stacks_members",
        "stacks_stack_ports",
    ],
    "port_channels": [
        "inbound_balancing_table",
        "member_status_table",
        "mlag_cisco_vpc",
        "mlag_pairs",
        "mlag_peers",
        "mlag_switches",
        "outbound_balancing_table",
    ],
    "qos": [
        "marking",
        "policing",
        "policy_maps",
        "priority_queuing",
        "queuing",
        "random_drops",
        "shapping",
    ],
    "routing": [
        "bgp_address_families",
        "bgp_neighbors",
        "eigrp_interfaces",
        "eigrp_neighbors",
        "isis_interfaces",
        "isis_neighbors",
        "ospf_interfaces",
        "ospf_neighbors",
        "ospfv3_interfaces",
        "ospfv3_neighbors",
        "path_lookup_checks",
        "rip_interfaces",
        "rip_neighbors",
        "route_stability",
        "routes_ipv4",
        "routes_ipv6",
        "summary_protocols",
        "summary_protocols_bgp",
        "summary_protocols_eigrp",
        "summary_protocols_isis",
        "summary_protocols_ospf",
        "summary_protocols_ospfv3",
        "summary_protocols_rip",
        "vrf_detail",
        "vrf_interfaces",
        "vrf_summary",
    ],
    "sdn": [
        "aci_dtep",
        "aci_endpoints",
        "aci_vlan",
        "aci_vrf",
        "apic_applications",
        "apic_bridge_domains",
        "apic_contexts",
        "apic_contracts",
        "apic_controllers",
        "apic_endpoint_groups",
        "apic_endpoint_groups_contracts",
        "vxlan_interfaces",
        "vxlan_peers",
        "vxlan_vni",
        "vxlan_vtep",
    ],
    "sdwan": ["links", "sites"],
    "security": [
        "acl",
        "acl_global_policies",
        "acl_interface",
        "dhcp_snooping",
        "dhcp_snooping_bindings",
        "dmvpn",
        "ipsec_gateways",
        "ipsec_tunnels",
        "secure_ports_devices",
        "secure_ports_interfaces",
        "secure_ports_users",
        "zone_firewall_interfaces",
        "zone_firewall_policies",
    ],
    "stp": [
        "bridges",
        "guards",
        "inconsistencies",
        "inconsistencies_details",
        "inconsistencies_multiple_stp",
        "inconsistencies_ports_multiple_neighbors",
        "inconsistencies_ports_vlan_mismatch",
        "inconsistencies_stp_cdp_ports_mismatch",
        "instances",
        "neighbors",
        "ports",
        "stability",
        "vlans",
    ],
    "vlans": [
        "device_detail",
        "device_summary",
        "l3_gateways",
        "network_summary",
        "site_summary",
    ],
    "wireless": [
        "access_points",
        "clients",
        "controllers",
        "radios_detail",
        "radios_ssid_summary",
    ],
}

tables = []

for k, v in choices.items():
    tables.extend(v)


def handle_module(ipf):
    technology = ipf.module.params['technology']
    table = ipf.module.params['table']
    filter = ipf.module.params['filter']
    columns = ipf.module.params['columns']
    report = ipf.module.params['report']
    sort = ipf.module.params['sort']
    snapshot_id = ipf.module.params['sort']

    if table not in choices[technology]:
        ipf.module.fail_json(
            f"{table} is not in the {technology} group. Available choices are {choices[technology]}")

    tech = getattr(ipf.ipf.technology, technology)
    table = getattr(tech, table)

    try:
        data = table.all(filters=filter, columns=columns, sort=sort, reports=report, snapshot_id=snapshot_id)
    except Exception as e:
        ipf.module.fail_json(f"Reponse Code: {e.response.json()['code']}. Message: {e.response.json()['message']}. Please check columns and or filters")

    ipf.module.exit_json(changed=False, data=data)


def main():
    argument_spec = AnsibleIPFModule.provider_argument_spec()
    argument_spec.update(
        snapshot_id=dict(
            type="str", 
            required=False
        ),
        technology=dict(
            type="str",
            required=True,
            choices=list(choices.keys()),
        ),
        table=dict(
            type="str",
            required=True,
            choices=tables,
        ),
        filter=dict(
            type="dict",
            required=False,
            default={},
        ),
        columns=dict(
            type="list",
            required=False,
            default=[],
            elements="str"
        ),
        sort=dict(
            type="dict",
            required=False,
            default={}
      ),
        report=dict(
            type='str',
            required=False
      )
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    IPFHelper = AnsibleIPFModule(module)

    handle_module(IPFHelper)


if __name__ == "__main__":
    main()
