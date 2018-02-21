from config import config

with open(config['shadowsocks_log_path'] + "/shadowsocks.log") as f:
    for line in f:
        list_of_content = str(line).split(' ')
        try:
            list_of_content[0] + list_of_content[1]
        except:
            print line
            print list_of_content
