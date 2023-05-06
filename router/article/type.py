from typing import List

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Article

ArticleGetAll = pydantic_model_creator(Article, name="文章查询返回模型")

# 创建、更新模型
ArticleCreate = pydantic_model_creator(Article, name="文章创建、修改模型",
                                       exclude=("create_time", "update_time", "path",))

# 前端返回全部文章模型
ArticleLists = pydantic_model_creator(Article, exclude=("description", "content", "view", "font_count", "is_show",))


# 创建文章与关联标签
class ArticleCreateWithTags(ArticleCreate):
    tags: list[int] = []


# 单篇文章查询返回模型
class ArticleGet(ArticleGetAll):
    tag: list[str] = []


class ArticleList(ArticleLists):
    tag: list[str] = []


class Article_list(BaseModel):
    page: str
    page_size: str
    total: str
    countPage: str
    data: List[ArticleList]
