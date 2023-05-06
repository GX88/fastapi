import datetime
from fastapi import APIRouter
from models import Log
from .type import LogGetAll, LogList
from utils import paginate
from router.ResponseType import R

log = APIRouter(prefix='/log')


@log.get('/list', summary="查询全部日志", response_model=R[LogList])
async def index(page: int = 1, page_size: int = 10):
    filters = {
        'andlist': {
            'create_time__gte': datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d"),
        }
    }
    a = await paginate(Log, LogGetAll, filters=filters, order_list=['-id'], page=page, page_size=page_size)
    return R.unified_response(200, a)
