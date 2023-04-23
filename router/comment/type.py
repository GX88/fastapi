from typing import List

from tortoise.contrib.pydantic import pydantic_model_creator
from models import Comment

GetAll = pydantic_model_creator(Comment, name="评论基础模型")

# 创建、更新模型
Create = pydantic_model_creator(Comment, name="评论创建、修改模型", exclude_readonly=True,
                                       exclude=("create_time", "update_time",))


class CommentList(GetAll):
    children: List[GetAll]
