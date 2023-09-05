import itchat
from itchat.content import *
from baidu_wenxin_api import get_response
#白名单
white_list = ['张三',
              '李四'
              ]

@itchat.msg_register(itchat.content.TEXT,isFriendChat=True)
def tuling_reply(msg):
    reply = get_response(msg['Text'])
    defaultReply = '我是百度研发的知识增强大语言模型文心一言(ERNIE Bot)，请向管理员申请白名单。'

    print(msg['User']['NickName'] + ':' + msg['Text'] )
    

    if msg['User']['NickName'] in white_list:
        print('Reply to ' + msg['User']['NickName'] + ':' + reply)
        print('')
        return reply
    else:
        print('Reply to ' + msg['User']['NickName'] + '我是百度研发的知识增强大语言模型文心一言(ERNIE Bot)，请向管理员申请白名单。')
        print('')
        return defaultReply

itchat.auto_login()
itchat.run()

