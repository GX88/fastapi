from fastapi import APIRouter
from .article.index import article
from .test import test

Router = APIRouter()

# 聚合
Router.include_router(article, tags=["文章接口"])
Router.include_router(test, tags=["测试接口s"])