from all import *
#kullanilmiyor
def multi_check(string, show_run):
    for i in show_run.split('!'):
        if string.split('\n')[0] in i.strip().split('\n')[0]:
            check_field = i
            for j in string.split('\n')[1:]:
                if j not in check_field:
                    return False
            return True
    return False

#kullanilmiyor
def print_both(name, single, multi):
    print(name, 'Single_line:', *single, 'Multiple_lines:', *multi , sep='\t')

#kullanilmiyor
def single_check(string, show_run):
    if string not in show_run: return False
    else: return True

def command_to_list(commands):
    single_line = list()
    multi_line = list()
    temp = str()
    intended = False
    for index, value in reversed(list(enumerate(commands))):
        if value[0] == ' ' or value[0] == '\t':
            intended = True
            if temp == '': temp = value.strip()
            else: temp = f'{value.strip()}\n{temp}'
        elif intended:
            intended = False
            multi_line.insert(0, f'{value.strip()}\n{temp}')
            temp = str()
        else:
            single_line.insert(0, value.strip())
    return multi_line, single_line

def single_check_verbose(string, show_run):
    status = 'Yok'
    fazla = list()
    if '\n' not in string:
        for i in show_run.split('\n'):
            if string == i.strip(): status = 'Var'; fazla.append(i.strip())
            elif string in i.strip(): fazla.append(i.strip())
        if string in fazla and len(fazla) > 1:
            fazla.remove(string)
            return ':'.join(['fazla',*fazla])
        elif string not in fazla and fazla:
            return ':'.join(['Farkli', *fazla])
        else: return status
    else:
        pass

def multi_find(string, show_run):
    for i in show_run.split('!'):
        if string.split('\n')[0] in i.strip().split('\n')[0]:
            return i.strip()
    return str()

def multi_check_verbose(string, show_run):
    show_run = multi_find(string, show_run)
    for i in string.split('\n')[1:]:
        yield single_check_verbose(i.strip(), show_run)

telco = connection(username='Abdulhamid.oksuz', password='Aralik2020', device_type='cisco_ios')
telco.read_ip_list()
telco.read_commands()

multi_line, single_line = command_to_list(telco.commands)
with open(f'{telco.log_dir}single_line_report.txt', 'a') as f:
    f.write('\t'.join(['Name', 'ip', *single_line])+'\n')
for i in multi_line:
    with open(telco.log_dir + i.split("\n")[0]+'.txt', 'a') as f:
        f.write('\t'.join(['Name', 'ip', *i.split('\n')[1:]]) + '\n')

show_run = """!
aa server falan 2
aa server falan 2 3
aaa authent server radius
!
isis 1
  network entity 1.11.111
  type broadcast
!
bbbb bbbb bbbb
cccc cccc cccc
!
bgp 65000
  e-bgp peer 2.2.2.2
  unicast-family ipv4
    enable
!
ddd ddd ddd
ee ee eee
!
"""
for ip in telco.ip_list:
    telco.login_enable(ip)
    telco.command('show run')
    show_run = telco.lastoutput
    telco.logout()
    with open(f'{telco.log_dir}single_line_report.txt', 'a') as f:
        f.write('\t'.join([telco.name, ip])+'\t')
        for i in single_line:
            f.write(single_check_verbose(i, show_run)+'\t')
        f.write('\n')
    for i in multi_line:
        with open(telco.log_dir + i.split("\n")[0]+'.txt', 'a') as f:
            f.write('\t'.join([telco.name, ip]) + '\t')
            for j in multi_check_verbose(i, show_run):
                f.write(j+'\t')
            f.write('\n')
