from __future__ import (absolute_import, division, print_function)

from ansible.module_utils.basic import env_fallback
import traceback
from ansible.module_utils.basic import missing_required_lib

from ansible.module_utils._text import to_native


__metaclass__ = type

table_choices = {
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
    "inventory": [
        'devices',
        'families',
        'fans',
        'hosts',
        'interfaces',
        'models',
        'modules',
        'os_version_consistency',
        'phones',
        'platforms',
        'pn',
        'sites',
        'vendors'
    ],
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

all_tables = []

for k, v in table_choices.items():
    all_tables.extend(v)

BOTO3_IMP_ERR = None
try:
    from ipfabric import IPFClient
    from ipfabric import models as ipf_models
    HAS_IPFABRIC = True
except ImportError:
    IPFABRIC_IMP_ERR = traceback.format_exc()
    HAS_IPFABRIC = False

HTTPX_IMP_ERR = None
try:
    import httpx
    HAS_HTTPX = True
except ImportError:
    HTTPX_IMP_ERR = traceback.format_exc()
    HAS_HTTPX = False


class AnsibleIPFError(Exception):

    def __str__(self):
        if self.exception and self.message:
            return "{0}: {1}".format(self.message, to_native(self.exception))

        return super().__str__()

    def __init__(self, message=None, exception=None, **kwargs):
        if not message and not exception:
            super().__init__()
        elif not message:
            super().__init__(exception)
        else:
            super().__init__(message)

        self.exception = exception
        self.message = message

        self.kwargs = kwargs or {}


class AnsibleIPFClientError(AnsibleIPFError):
    pass


def check_sdk():
    if not HAS_IPFABRIC:
        raise AnsibleIPFClientError(message=missing_required_lib('ipfabric'))

    if not HAS_HTTPX:
        raise AnsibleIPFClientError(message=missing_required_lib('ipfabric'))

    return IPFClient


def get_client(**kwargs):
    try:
        ipf = IPFClient(**kwargs, unloaded=True)
        models = ipf_models
    except httpx.HTTPStatusError as exc:
        raise AnsibleIPFClientError(message=f"Failed to connect: {exc.response.json()['message']} ({exc.response.json()['code']})")
    except httpx.ConnectTimeout as exc:
        raise AnsibleIPFClientError(message=f"Failed to connect: {exc}")

    return ipf, models


class AnsibleIPFModule(object):
    """An ansible module class for IP Fabric modules
    AnsibleIPFModule provides a class for building modules which
    connect to IP Fabric.
    """

    def __init__(self, module):
        self.module = module
        self.provider = module.params.get('provider')

        check_sdk()

        client, models = get_client(**self.provider)
        self.ipf = client
        self.models = models

    def get_snapshot(self, snapshot_id):
        return self.ipf.get_snapshot(snapshot_id=snapshot_id)

    def get_snapshots_list(self):
        resp = self.ipf.get_snapshots()
        return_list = []
        for k, v in resp.items():
            if k not in ['$last', '$prev']:
                return_list.append(v.dict())

        return return_list

    def table_info(self, technology, table, filter, columns, report, sort, snapshot_id):
        if table not in table_choices[technology]:
            self.module.fail_json(
                f"{table} is not in the {technology} group. Available choices are {table_choices[technology]}")

        if technology == 'inventory':
            table = getattr(self.ipf.inventory, table)
        else:
            tech = getattr(self.ipf.technology, technology)
            table = getattr(tech, table)

        try:
            data = table.all(filters=filter, columns=columns, sort=sort, reports=report, snapshot_id=snapshot_id)
        except Exception as e:
            self.module.fail_json(f"Reponse Code: {e.response.json()['code']}. Message: {e.response.json()['message']}. Please check columns and or filters")

        return data

    @staticmethod
    def provider_argument_spec():
        return dict(
            provider=dict(
                type="dict",
                options=dict(
                    base_url=dict(
                        type='str',
                        required=True,
                        fallback=(env_fallback, ['IPF_URL'])
                    ),
                    token=dict(type="str", required=True, fallback=(env_fallback, ['IPF_TOKEN']), no_log=True),
                    api_version=dict(type="str", required=False),
                    verify=dict(type="bool", required=False, default=True)
                    timeout=dict(type='int', required=False, default=None)
                ),
                required=True
            )
        )
