from fastapi import APIRouter
from models import Log
from .type import LogGetAll
from utils import paginate

log = APIRouter(prefix='/log')


@log.get('', summary="查询全部日志")
async def index():
    a = await paginate(Log, order_list=['-id'] ,page=6, page_size=10)
    return a
