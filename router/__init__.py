from fastapi import APIRouter
from .article.index import article
from .log.index import log
from .test import test

Router = APIRouter(prefix='/api')

# 聚合
Router.include_router(article, tags=["文章接口"])
Router.include_router(log, tags=["日志接口"])
Router.include_router(test, tags=["测试接口"])