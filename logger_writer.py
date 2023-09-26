#UTF-8
# 直接把内容放在函数括号里即可

import time

def log_writer(content_text):
    f = open('E:/Cache/VSCode/Code/baidu_wenxin/wechat_log.txt', 'a',encoding='GB2312')
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + ' ' + content_text + '\n')
    f.close()


