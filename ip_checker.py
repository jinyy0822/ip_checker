import datetime


# Read the white list
ip_white_list = set()
# with open("ip_white_list.csv") as f:
with open("/root/checking_for_ip/ip_white_list.csv") as f:
    for line in f:
        ip_white_list.add(str(line).split('\r')[0])
print 'ip_white_list: ', list(ip_white_list), '\r\n'


# check all the ip
ip_pool = set()
# with open("shadowsocks.log") as f:
with open("/var/log/shadowsocks.log") as f:
    for line in f:
        list_of_content = str(line).split(' ')
        if list_of_content[2] == 'INFO' and list_of_content[-2] == 'from':
            ip = list_of_content[-1].split(':')[0]
            ip_pool.add(ip)
print 'ip_have_accessed: ', list(ip_pool), '\r\n'


# check for unusual ip
for ip in list(ip_pool):
    if ip not in ip_white_list:
        print'Nowtime in Beijing: ' + str(datetime.datetime.utcnow()
                                                         + datetime.timedelta(hours=8)) + '\r\n'
        print'Found unusual IP Address: ' + ip + '\r\n'
        with open("/root/checking_for_ip/log.txt", 'a') as fl:
            fl.write('Nowtime in Beijing: ' + str(datetime.datetime.utcnow()
                                                 + datetime.timedelta(hours=8)) + '\r\n')
            fl.write('Found unusual IP Address: ' + ip + '\r\n')
