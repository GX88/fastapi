from fastapi import APIRouter
from typing import List
from models import Article
from .type import ArticleGetAll, ArticleCreate

article = APIRouter(prefix='/article')


@article.get('', summary="查询全部文章", response_model=List[ArticleGetAll])
async def index():
    a = await Article.all()
    return a


@article.post('', summary="创建文章")
async def index(model: ArticleCreate):
    a = await Article.create(**model.dict())
    return a
