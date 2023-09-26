#UTF-8

import itchat
import time
from itchat.content import *
from logger_writer import log_writer
from baidu_wenxin_api import get_response
from txt_to_list import white_list_reader


#msg_receive = 'hello world'
#msg_send = get_response(msg_receive)
#itchat.send(msg_send, toUserName='filehelper')

@itchat.msg_register(itchat.content.TEXT,isFriendChat=True)
def tuling_reply(msg):
    reply = get_response(msg['Text'])
    defaultReply = '我是百度研发的知识增强大语言模型文心一言(ERNIE Bot)，请向管理员申请白名单。'
    
    auto_ques = ' ' + msg['User']['NickName'] + ':' + msg['Text'] 

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),end = '')
    print(auto_ques)
    log_writer(auto_ques)

    white_list = white_list_reader('E:/Cache/VSCode/Code/baidu_wenxin/white_list.txt')
    
    if msg['User']['NickName'] in white_list:
        auto_reply = ' ' + 'Reply to ' + msg['User']['NickName'] + ':' + reply
        log_writer(auto_reply)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),end = '')
        print(auto_reply)
        print('')
        return reply
    else:
        auto_reply = ' ' + 'Reply to ' + msg['User']['NickName'] + '我是百度研发的知识增强大语言模型文心一言(ERNIE Bot)，请向管理员申请白名单。'
        log_writer(auto_reply)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),end = '')
        print(auto_reply)
        print('')
        return defaultReply
    


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login() #hotReload=True
itchat.run()

