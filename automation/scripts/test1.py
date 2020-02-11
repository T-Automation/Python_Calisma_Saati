from all import *
import time 

connect = connection('onur.aksoy', 'Ekim.2019', 'cisco_ios')
connect.read_ip_list()
connect.read_commands()
for i in connect.ip_list:
    changed_int_count = 0
    connect.login_enable(i)
    connect.command('show run', expect=connect.name+'#')
    connect.log_save()
