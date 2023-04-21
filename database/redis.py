#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 20:34
# @Author  : CoderCharm
# @File    : sys_redis.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

通过class 实例化对象可以直接修改内部属性的特性
再通过魔法方法，赋予实例化对象 具有内部属性_redis_client的方法和属性

主要参考 flask-redis扩展实现
https://github.com/underyx/flask-redis/blob/master/flask_redis/client.py

redis 连接

"""
import sys
from redis import Redis, AuthenticationError


class RedisCli(object):

    def __init__(self, *, host: str, port: int, password: str, db: int, socket_timeout: int = 5):
        # redis对象 在 @app.on_event("startup") 中连接创建
        self._redis_client = None
        self.logger = None
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.socket_timeout = socket_timeout

    def init_redis_connect(self, logger) -> None:
        """
        初始化连接
        :return:
        """
        try:
            self._redis_client = Redis(
                host=self.host,
                port=self.port,
                password=self.password,
                db=self.db,
                socket_timeout=self.socket_timeout,
                decode_responses=True  # 解码
            )
            if not self._redis_client.ping():
                logger.error("redis连接失败")
            logger.info("redis连接成功")
        except (AuthenticationError, Exception) as e:
            logger.error(f"redis连接失败: {e}")

    def close(self) -> None:
        self._redis_client.close()

    # 使实例化后的对象 赋予redis对象的的方法和属性
    def getattr(self, name):
        return getattr(self._redis_client, name)

    def getitem(self, name):
        return self._redis_client[name]

    def setitem(self, name, value):
        self._redis_client[name] = value

    def delitem(self, name):
        del self._redis_client[name]

    def compare(self, name, captcha):
        return self.getitem(name).lower() == captcha.lower()


# 创建redis连接对象
redis_client = RedisCli(
    host='43.155.168.243',
    port=6379,
    password='199907173030bz',
    db=0,
    socket_timeout=5
)

# 只允许导出 redis_client 实例化对象
__all__ = ["redis_client"]
