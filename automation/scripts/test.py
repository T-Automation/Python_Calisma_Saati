from all import *

connect = connection('onur.aksoy', 'Ekim.2019', 'cisco_ios')
ip_list = connect.read_ip_list()
commands = connect.read_commands()
connect.run_commands()