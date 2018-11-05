import time
import string


def log(action):
    time_dic = time.localtime(time.time())
    log_message = '[ {}:{}:{} ] {}'.format(time_dic.tm_hour, time_dic.tm_min, time_dic.tm_sec, string.log_dict[action])
    print(log_message, end='')


log('high_start')
