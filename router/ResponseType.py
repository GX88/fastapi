#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 20:34
# @Author  : 白哲
# @File    : unifiedResponse.py
# @Software: PyCharm
# @Desc    : 实现统一响应


from typing import Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")

codeMsg = {
    200: 'success',
    400: 'fail',
    401: 'unauthorized',
    403: 'forbidden',
    404: 'not found',
    405: 'method not allowed',
    500: 'internal server error',
}


class R(GenericModel, Generic[T]):
    code: int
    data: T
    msg: str

    @staticmethod
    def unified_response(code, data: T = None) -> "R":
        return R(code=code, msg=codeMsg[code], data=data)
