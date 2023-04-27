#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/04/23 09:45
# @Author  : Faith
# @File    : dev.py
# @Software: PyCharm
# @Email   : gxlove_max@163.com
# @Desc    : 开发模式配置

import os


# MySQL
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'fastapi'
MYSQL_PASSWORD = '199907173030bz'
MYSQL_DB = 'fastapi'

# Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = '199907173030bz'
REDIS_SOCKET_TIMEOUT = 5

# 项目配置
APP_HOST = '127.0.0.1'
APP_PORT = 8010
APP_DEBUG = False
APP_RELOAD = False
DOCS_URL = '/docs'
DOCS_TITLE = '白哲PM | API'
DOCS_DESC = 'API文档'

# CORS
ORIGINS = ['http://127.0.0.1']

# 项目根路径
BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
