from fastapi import APIRouter
from typing import List
from models import Article, Tag
from .type import ArticleGetAll, ArticleCreateWithTags

article = APIRouter(prefix='/article')


@article.get('', summary="查询全部文章", response_model=List[ArticleGetAll])
async def index():
    a = await Article.all()
    return a


@article.post('', summary="创建文章")
async def index(model: ArticleCreateWithTags):
    tag_list = model.tags
    del model.tags
    post = await Article.create(**model.dict())
    if tag_list:
        for tag in tag_list:
            tag = await Tag.get(id=tag)
            await post.tags.add(tag)
    return post
