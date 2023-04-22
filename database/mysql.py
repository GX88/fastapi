from tortoise.exceptions import DBConnectionError
from tortoise.contrib.fastapi import register_tortoise

ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': "localhost",
                'user': "root",
                'password': "199907173030bz",
                'port': 3306,
                'database': "fastapi",
            }
        }
    },
    "apps": {
        "base": {
            "models": ["aerich.models", "models"],
            "default_connection": "base"
        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app):
    # 注册数据库

    register_tortoise(
        app,
        config=ORM_CONFIG,
        generate_schemas=False,
        add_exception_handlers=False,
    )
    app.logger.info("数据库连接成功")
