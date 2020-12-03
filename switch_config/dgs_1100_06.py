ip_address = input("Введите ip коммутатора: ")
switch_name = input("Введите имя коммутатора: ")
manager_vlan = input("Введите manager-vlan: ")
untagged_vlan = input("Введите пользовательский vlan: ")
tagged_vlan = input("Введите vlan'ы в таггете (пример хххх,хххх,хххх): ")
ip_network = '.'.join(ip_address.split('.')[:-1]) + '.1'


config = '''
#
create account admin sbnt
PASSWD
PASSWD
!
enable password encryption
!
#
config command_prompt ''' + switch_name + '''
config snmp system_name ''' + switch_name + '''_''' + ip_address + '''
config snmp system_contact Tel:11-22-33-44
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
#
enable loopdetect
config loopdetect mode portbase
config loopdetect ports 1-3 state enable
config loopdetect interval_time 2 lbd_recover_time 1800
#
enable bpdu_protection
config bpdu_protection recovery_timer 1800
config bpdu_protection log attack_detected
config bpdu_protection ports 1-3 state enable mode drop
#
config traffic_segmentation 1-3 forward_list 6
create access_profile ip udp src_port_mask 0xFFFF profile_id 1
config access_profile profile_id 1 add access_id 1 ip udp src_port 67 port 1-3 deny
config port_security 1-3 admin_state enable max_learning_addr 3 lock_address_mode DeleteOnTimeout
#
delete snmp community public
delete snmp community private
create snmp community subnet911 ReadOnly
#
enable lldp
config lldp ports 6 notification enable
config lldp ports 6 admin_status tx_and_rx
config lldp ports 6 basic_tlvs port_description system_name system_description system_capabilities enable
#
config sntp primary 81.163.*.* secondary 0.0.0.0 poll-interval 3600
config time_zone operator + hour 3 minute 0
config dst disable
enable sntp 
#
# Access authentication control
enable authen_policy
enable aaa_server_password_encryption
config authen parameter response_timeout 30
config authen parameter attempt 3
create authen server_host 10.11.*.* protocol tacacs+ port 49 key PASSWD timeout 2
create authen server_group tacacs+
config authen server_group tacacs+ add server_host 10.11.*.* protocol tacacs+
create authen_login method_list_name tac_plus
config authen_login method_list_name tac_plus method tacacs+ local
create authen_enable method_list_name tac_plus_ena
config authen_enable method_list_name tac_plus_ena method tacacs+ local
config authen application console login method_list_name tac_plus
config authen application telnet login method_list_name tac_plus
config authen application ssh login method_list_name tac_plus
config authen application http login method_list_name tac_plus
config authen application console enable method_list_name tac_plus_ena
config authen application telnet enable method_list_name tac_plus_ena
config authen application ssh enable method_list_name tac_plus_ena
config authen application http enable method_list_name tac_plus_ena
#
# Accounting
create accounting method_list_name tac_plus
config accounting method_list_name tac_plus method tacacs+ none
config accounting service network state enable method_list_name tac_plus
config accounting service shell state enable method_list_name tac_plus
config accounting service system state enable method_list_name tac_plus
config accounting service command administrator method_list_name tac_plus
config accounting service command operator method_list_name tac_plus
config accounting service command power_user method_list_name tac_plus
config accounting service command user method_list_name tac_plus

save
'''
