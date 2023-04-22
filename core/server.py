from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import register_mysql, redis_client
from core.middle import Middle
from router import Router
from utils import logger


class MyFastAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger
        self.redis = redis_client


def create_app() -> MyFastAPI:
    app = MyFastAPI()

    # TODO: 添加事件监听事件
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
        app.logger.info("fastapi正在启动")

        # TODO: 初始化数据连接
        await register_mysql(app)
        # TODO: 初始化redis连接
        app.redis.init_redis_connect(app.logger)

    @app.on_event("shutdown")
    async def stopping() -> None:
        """
        关闭事件
        :return: None
        """
        app.redis.close()
        app.logger.info("fastapi已关闭\n")


def register_middleware(app: MyFastAPI):
    """
    注册中间件
    :return: None
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.add_middleware(Middle)
