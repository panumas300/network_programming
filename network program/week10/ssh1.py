from netmiko import ConnectHandler

SW4 = {
    'device_type':'cisco_ios',
    'ip':'123.123.123.115',
    'username':'cisco',
    'password':'cisco'
}

net_connect = ConnectHandler(**SW4)

output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(2,21):
    print('Creating VLAN ' + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)