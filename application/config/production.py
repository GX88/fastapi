#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/04/23 09:45
# @Author  : Faith
# @File    : production.py
# @Software: PyCharm
# @Email   : gxlove_max@163.com
# @Desc    : 生产模式配置

import os

# MySQL
MYSQL_ENABLE = False
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'fastapi'
MYSQL_PASSWORD = '199907173030bz'
MYSQL_DB = 'fastapi'

# Redis
REDIS_ENABLE = False
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = '199907173030bz'
REDIS_SOCKET_TIMEOUT = 5

# MongoDB
MONGODB_ENABLE = False
MONGODB_HOST = 'localhost'
MONGODB_DB = "kinit"
MONGODB_USER = "kinit"
MONGODB_PASSWORD = "199907173030bz"

# 项目配置
APP_HOST = '127.0.0.1'
APP_PORT = 8010
APP_DEBUG = True
APP_RELOAD = True
DOCS_URL = None
REDOCS_URL = None
DOCS_TITLE = 'NebAdmin | API'
DOCS_DESC = 'API文档'

# 项目根路径
BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

"""
阿里云对象存储OSS配置
阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
 *  [accessKeyId] {String}：通过阿里云控制台创建的AccessKey。
 *  [accessKeySecret] {String}：通过阿里云控制台创建的AccessSecret。
 *  [bucket] {String}：通过控制台或PutBucket创建的bucket。
 *  [endpoint] {String}：bucket所在的区域， 默认oss-cn-hangzhou。
"""
ALIYUN_OSS = {
    "accessKeyId": "accessKeyId",
    "accessKeySecret": "accessKeySecret",
    "endpoint": "endpoint",
    "bucket": "bucket",
    "baseUrl": "baseUrl"
}

"""
获取IP地址归属地
文档：https://user.ip138.com/ip/doc
"""
IP_PARSE_ENABLE = False
IP_PARSE_TOKEN = "IP_PARSE_TOKEN"
