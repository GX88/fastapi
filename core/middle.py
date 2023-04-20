# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: Faith
@Des: 中间件
"""
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request


class ApiLogger(object):
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] not in ["http", "websocket"]:
            await self.app(scope, receive, send)
            return

        print(scope['client'][0])
        # 获取请求浏览器
        user_agent = scope['headers'][5][1].decode()
        print(user_agent)

        # 打印请求来源

        req = Request(scope, receive, send)

        async def send_wrapper(message: Message) -> None:
            if message['type'] == 'http.response.start':
                # 获取响应状态码
                status_code = message['status']
                if 200 <= status_code < 400:
                    # 如果请求成功，则打印请求成功信息
                    print(status_code, user_agent)
                else:
                    # 如果请求失败，则打印请求失败信息
                    print("Request failed")

            await send(message)

        await self.app(scope, receive, send_wrapper)
