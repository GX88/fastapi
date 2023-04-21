import math
from typing import List
from tortoise.expressions import Q
from tortoise.models import Model


async def paginate(
        model: Model,
        order_list: List = None,
        page: int = 1,
        page_size: int = 10, ):

    q = Q()

    a = ['-id', '-create_time']
    # 总页
    total = await model.filter(q).count()
    # 页数
    countPage = math.ceil(total / page_size)

    data = await model.filter(q).order_by(*order_list).offset((page - 1) * page_size).limit(page_size).values(*a)

    return {
        'data': data,
        'page': page,
        "page_size": page_size,
        'total': total,
        'countPage': countPage,
    }
