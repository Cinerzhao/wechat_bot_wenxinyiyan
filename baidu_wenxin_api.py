import requests
import json
import random
import time

def get_response(msg):
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": msg
            },
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    to_wechat = json.loads(response.text).get('result')
    #随机延迟防封号
    delay = random.randrange(0,100,1)/100
    time.sleep(delay)
    return to_wechat
    

def get_access_token():
    #填入您的百度API_KEY和SECRET_KEY
    API_KEY = ""
    SECRET_KEY = ""

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
