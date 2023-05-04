from fastapi import APIRouter
from typing import List
from models import Log
from .type import LogGetAll, LogList
from utils import paginate
from router.ResponseType import R

log = APIRouter(prefix='/log')


@log.get('/list', summary="查询全部日志", response_model=R[LogList])
async def index(page: int = 1, page_size: int = 10):
    a = await paginate(Log, LogGetAll, order_list=['-id'], page=page, page_size=page_size)
    b = R.unified_response(200, a)
    return b
