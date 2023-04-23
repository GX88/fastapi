from tortoise.contrib.fastapi import register_tortoise
import config as f

ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': f.MYSQL_HOST,
                'user': f.MYSQL_USER,
                'password': f.MYSQL_PASSWORD,
                'port': f.MYSQL_PORT,
                'database': f.MYSQL_DB,
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
