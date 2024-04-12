# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: Faith
@Des: 中间件
"""
from fastapi import Request, FastAPI
from application.settings import OPERATION_RECORD_METHOD, IGNORE_OPERATION_FUNCTION, \
    DEMO_WHITE_LIST_PATH, DEMO
from utils.response import ErrorResponse


# 演示环境中间件，取消所有POST,DELETE,PUT操作权限
def demo_middleware(app: FastAPI):
    """
    演示环境中间件，取消所有POST,DELETE,PUT操作权限
    :param app: FastAPI
    :return: None
    """

    @app.middleware("http")
    async def demo(request: Request, call_next):
        path = request.scope.get("path")
        if request.method != "GET" and path not in DEMO_WHITE_LIST_PATH:
            return ErrorResponse(msg="演示环境，不支持此操作")
        return await call_next(request)

    return app
