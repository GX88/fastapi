from typing import List

from fastapi import APIRouter
from models import Comment
from router.ResponseType import R
from .type import CommentList, Create

comment = APIRouter(prefix='/comment')


@comment.get('', summary='获取评论列表', description='获取文章评论列表', response_model=R[List[CommentList]])
async def get_comment(article_id: int):
    result = await Comment.filter(ArticleID=article_id).order_by('id').values()
    root = [i for i in result if i['cid'] == 0]
    child = [i for i in result if i['cid'] != 0]
    data = []

    for item in root:
        root_nodes = item
        root_nodes['children'] = []

        for i in child:
            if item['id'] == i['cid']:
                root_nodes['children'].append(i)
        data.append(root_nodes)

    return R.unified_response(200, data=data)


@comment.post('', summary='创建评论', description='创建文章评论')
async def create_comment(item: Create):
    await Comment.create(**item.dict())
    return R.unified_response(200)
