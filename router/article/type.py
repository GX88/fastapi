from tortoise.contrib.pydantic import pydantic_model_creator
from models import Article

ArticleGetAll = pydantic_model_creator(Article, name="文章查询返回模型")

# 创建、更新模型
ArticleCreate = pydantic_model_creator(Article, name="文章创建、修改模型", exclude_readonly=True,
                                       exclude=("create_time", "update_time",))


# 创建文章与关联标签
class ArticleCreateWithTags(ArticleCreate):
    tags: list[int] = []


# 单篇文章查询返回模型
class ArticleGet(ArticleGetAll):
    tag: list[str] = []
