import math
from typing import List, Dict

from tortoise.expressions import Q
from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.query_utils import Prefetch


# TODO：待实现多AND与多AND的AND ｜ OR；
# TODO：多OR与多OR的OR ｜ AND；
async def paginate(
        model: models,
        schema: pydantic_model_creator,
        filters: Dict = None,
        Prefetching: Dict = None,
        order_list: List = None,
        page: int = 1,
        page_size: int = 10,
):
    """
    分页
    :param model: 数据库模型
    :param schema: 验证模型类
    :param filters: 规则
    :param Prefetching: 预取
    :param order_list: 排序
    :param page: 页数
    :param page_size: 条数
    :return: 根据条件查询出的数据
    """

    """
    filters对应字段信息
    
    type字段默认为and，andlist为and条件，orlist为or条件
    addlist为字典，addlist中的所有属性都是and条件
    orlist为字典，orlist中的所有属性都是or条件
    
    当type为and时，andlist和orlist中的属性都是and条件
    当type为or时，andlist和orlist中的属性都是or条件
    
    type: str = Enum('and', 'or'),
    andlist: Dict = {},
    orlist: Dict = {},
    """

    if filters is None:
        filters = {
            'type': 'and',
            'andlist': {},
            'orlist': {},
        }
    else:
        if 'type' not in filters:
            filters['type'] = 'and'
        if 'andlist' not in filters:
            filters['andlist'] = {}
        if 'orlist' not in filters:
            filters['orlist'] = {}

    q = Q(**filters['andlist']) & Q(**filters['orlist']) if filters['type'] == 'and' \
        else Q(**filters['andlist']) | Q(**filters['orlist'])

    fields = list(schema.schema()['properties'].keys())

    # 总页
    total = await model.filter(q).count()
    # 页数
    countPage = math.ceil(total / page_size)

    if Prefetching:
        data = await model.filter(q) \
            .order_by(*order_list) \
            .offset((page - 1) * page_size).limit(page_size) \
            .prefetch_related(
                Prefetch(
                    Prefetching['name'],
                    queryset=Prefetching['queryset'].all()
                )
            )
        for i in data:
            i.tag = [j.name for j in i.tags]
    else:
        data = await model.filter(q) \
            .order_by(*order_list) \
            .offset((page - 1) * page_size).limit(page_size) \
            .values(*fields)

    return {
        'data': data,
        'page': page,
        "page_size": page_size,
        'total': total,
        'countPage': countPage,
    }
