from fastapi import APIRouter
from typing import List

from tortoise.query_utils import Prefetch

from models import Article, Tag
from .type import ArticleGetAll, ArticleCreateWithTags, ArticleGet
from ..ResponseType import R

article = APIRouter(prefix='/article')


@article.get('/all', summary="查询全部文章", response_model=List[ArticleGetAll])
async def index():
    post = await Article.all()
    return post


@article.get('', summary="查询单篇文章", response_model=R[ArticleGet])
async def index(aid: int):
    post = await Article.filter(id=aid).prefetch_related(
        Prefetch('tags', queryset=Tag.all())
    ).first()
    if post:
        post.tag = [i.name for i in post.tags]

    return R.unified_response(200, data=post)


@article.post('', summary="创建文章", response_model=R)
async def index(model: ArticleCreateWithTags):
    tag_list = model.tags
    del model.tags
    post = await Article.create(**model.dict())
    if tag_list:
        t = await Tag.filter(id__in=tag_list).all()
        await post.tags.add(*t)
    return R.unified_response(200)


@article.delete('', summary="删除文章", response_model=R)
async def index(aid: int):
    post = await Article.filter(id=aid).first()
    if post:
        await post.delete()
        await post.tags.clear()
    return R.unified_response(200)
