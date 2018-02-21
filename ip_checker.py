# -*- coding:utf-8 -*-


import datetime
import pygeoip
from config import config
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
gic = pygeoip.GeoIP(config['current_path'] + '/GeoLiteCity.dat')


def get_country_and_city(ip_address):
    global gic
    # noinspection PyBroadException
    try:
        res = gic.record_by_addr(ip_address)['country_name'] + ', ' + gic.record_by_addr(ip_address)['city']
    except:
        res = 'Unknown'
    return res


# Read the white list
ip_white_list = set()
with open(config['current_path'] + "/ip_white_list.csv") as f:
    for line in f:
        ip_white_list.add(get_country_and_city(str(line).split('\r')[0]))


# check all the ip
ip_pool = set()
with open(config['shadowsocks_log_path'] + "/shadowsocks.log") as f:
    for line in f:
        list_of_content = str(line).split(' ')
		print list_of_content[0] + list_of_content[1]
		print type(list_of_content[0] + list_of_content[1])
        content_datetime = datetime.datetime.strptime(list_of_content[0] + list_of_content[1], '%Y-%m-%d%H:%M:%S')
        if list_of_content[2] == 'INFO' and list_of_content[-2] == 'from' and \
                (datetime.datetime.now() - content_datetime).days <= 1:
            ip = list_of_content[-1].split(':')[0]
            ip_pool.add(ip)


# check for unusual ip
for ip in list(ip_pool):
    if get_country_and_city(ip) not in ip_white_list:
        print 'Unusual access within 1 day: ' + ip + ' from ' + get_country_and_city(ip) + '\r\n'


print 'Whitelist of cities: ', list(ip_white_list), '\r\n'
print 'Access within 1 day: ', list(ip_pool), '\r\n'
