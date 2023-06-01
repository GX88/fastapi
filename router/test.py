import hashlib
import random
import time

import requests
import string
from fastapi import APIRouter
from utils import SendEmail

test = APIRouter(prefix='/test')


@test.get('/jssdk')
async def config(url: str):
    appid = "wxfd3bcc7a6fd37518"
    appsceret = "6e0a10a04962f2bdea8ae20ff9c198d8"
    access_token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(
        appid, appsceret)

    # access_token = requests.get(access_token_url).json()

    access_token = "68_-EPYlaMloDBTqGIJVwFybaq_efhBEBkl8Dsud1154WB9cJ4ylBkCSEWytqLsHGtqetELCWr2Tj-STpZfXQOGffd8w4CA-gUu9P1cU91XIP1w7hQZD6tN9cZ8CjsWMUjACAJZH"

    ticket_url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={}&type=jsapi".format(access_token)

    # ticket = requests.get(ticket_url).json()

    ticket = "HoagFKDcsGMVCIY2vOjf9i-0tBOL1eO5Aet-WF7n4ZRdUsBfwOg7gf0sSRGe_WsY0EaIKhzPvHfhkNjTpfIIOw"

    # 利用random随机生成字符串
    noncestr = ''.join(random.sample(string.ascii_letters + string.digits, 16))

    timestamp = int(time.time())

    string1 = "jsapi_ticket={}&noncestr={}&timestamp={}&url={}".format(ticket, noncestr, timestamp, url)
    signature = hashlib.sha1(string1.encode('utf-8')).hexdigest()

    return {'code': "200", 'msg': "success", 'data': {
        'appId': appid,
        'timestamp': timestamp,
        'nonceStr': noncestr,
        'signature': signature,
        'ticket': ticket,
        'url': url,
    }}


@test.get('/mail')
async def mail():
    article = "测试文章"
    nickname = "张三"
    text = "这是一条测试评论"
    ip = "122.122.122.122"
    email = "akldjlkas@163.com"
    admin_url = "https://www.白哲.com"
    site = "白哲PM"
    send_email = SendEmail(['lyl_7210@163.com', '2016415409@qq.com'])
    await send_email.send(article=article, nickname=nickname, text=text, ip=ip, email=email, admin_url=admin_url,
                          site=site)
    return {'code': "200", 'msg': "success", 'data': {}}
