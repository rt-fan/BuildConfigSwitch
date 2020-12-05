
config2 = ''


def conf(ip_address, switch_name, manager_vlan, untagged_vlan, tagged_vlan):
    ip_network = '.'.join(ip_address.split('.')[:-1]) + '.1'
    config = '''
#
create account admin LOGIN
PASSWD
PASSWD
!
enable password encryption
!
#
config command_prompt ''' + switch_name + '''
config snmp system_name ''' + switch_name + '''_''' + ip_address + '''
config snmp system_contact Tel:99-99-99-99
config snmp system_location ''' + switch_name + '''
#
create vlan manager tag ''' + manager_vlan + '''
create vlan ''' + switch_name + ''' tag ''' + untagged_vlan + '''
config vlan vlanid ''' + manager_vlan + ''',''' + tagged_vlan + ''' add tag 6
config vlan vlanid ''' + untagged_vlan + ''' add untag 1-3
config vlan vlanid ''' + manager_vlan + ''' add untag 5
config vlan vlanid 1 delete 1-3,5-6
#
create iproute default ''' + ip_network + ''' 1
config ipif System ipaddress ''' + ip_address + '''/255.255.255.0 vlan manager
config ipv6 nd ns ipif System retrans_time 1
enable ipif_ipv6_link_local_auto System
config ipif System ipv6 state disable
#
enable dhcp_local_relay
config dhcp_local_relay port 1-3 state enable
config dhcp_local_relay vlan vlanid ''' + untagged_vlan + ''' state enable

save
'''
    global config2
    config2 = config
