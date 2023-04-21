from tortoise.contrib.pydantic import pydantic_model_creator
from models import Log

LogGetAll = pydantic_model_creator(Log, exclude=("create_time",), name="日志列表模型")

# 创建、更新模型
ArticleCreate = pydantic_model_creator(Log, name="文章创建、修改模型", exclude_readonly=True, exclude=("create_time", "update_time",))
