# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:08:26 2020

@author: erdemk
"""
from netmiko import ConnectHandler
import os

path_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'e', 'ip_adres_listesi.txt')
f = open(path_file, 'r')
dosya = f.read()
f.close()
device_list = dosya.split(' ')

for device in device_list:
    
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip':   device,
        'username': 'user_id',
        'password': 'password'
    }

    try:
        net_connect = ConnectHandler(**cisco_device)
        net_connect.enable()
        show_run = net_connect.send_command('show run')
        net_connect.disconnect()
        output = textfsm_temp.ParseText(show_run)

        path_file_kaydet = os.path.join(os.path.expanduser('~'), 'Desktop', 'e', 'show_run_'+device+'.txt')
        g = open(path_file_kaydet, 'w')
        print(show_run, file=g)
        g.close()
        print(device, ' ip li cihaza baglanildi ve show run kaydedildi.')
    except:
        print(device, ' ip li cihaza baglanilamadi')