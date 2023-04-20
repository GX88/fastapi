from fastapi import APIRouter, Request

test = APIRouter()


@test.get('/config')
async def config(request: Request):
    # request.app.redis.setitem("test", "test")
    # val = request.app.redis.getitem("test")
    return {'code': "200", 'msg': "success", 'data': 'val'}
