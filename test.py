import datetime
from config import config

with open(config['shadowsocks_log_path'] + "/shadowsocks.log") as f:
    for line in f:
        list_of_content = str(line).split(' ')
        try:
            content_datetime = datetime.datetime.strptime(list_of_content[0] + list_of_content[1], '%Y-%m-%d%H:%M:%S')
        except:
            print line
            print list_of_content[0]
            print list_of_content[1]
            print type(list_of_content[0])
            print type(list_of_content[1])
