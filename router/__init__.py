from fastapi import APIRouter
from .mock import mock

Router = APIRouter(prefix='/api')

# 聚合
Router.include_router(mock, tags=["mock接口"])
