from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import config as f
from utils import FileExecution

from database import register_mysql, redis_client
from core.middle import Middle
from router import Router
from utils import logger


class MyFastAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger
        self.redis = redis_client
        self.project_path = f.PROJECT_PATH


def create_app() -> MyFastAPI:
    app = MyFastAPI(
        debug=f.APP_DEBUG,
        title=f.DOCS_TITLE,
        description=f.DOCS_DESC,
        docs_url=f.DOCS_URL
    )

    # TODO: 各类事件初始化
    register_init(app)

    # TODO: 注册中间件
    register_middleware(app)

    # TODO: 注册路由
    app.include_router(Router)

    return app


def register_init(app: MyFastAPI):
    """
    初始化连接
    :param app: FastAPI
    :return: None
    """

    @app.on_event("startup")
    async def startup() -> None:
        """
        启动事件
        :return: None
        """
        app.logger.info("FastAPI已启动")

        # TODO: 执行数据库初始化
        await register_mysql(app)
        # TODO: 执行sql文件
        # FileExecution(app.project_path)
        # TODO: 初始化redis连接
        app.redis.init_redis_connect(app.logger)

    @app.on_event("shutdown")
    async def stopping() -> None:
        """
        关闭事件
        :return: None
        """
        app.redis.close()
        app.logger.info("FastAPI已关闭\n")


def register_middleware(app: MyFastAPI):
    """
    注册中间件
    :return: None
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=f.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.add_middleware(Middle)
