from fastapi import APIRouter

mock = APIRouter()


@mock.post('/login')
async def login(body: dict):
    if body.get('username') == "admin":
        return {
            'success': True,
            'data': {
                'username': "admin",
                'roles': ["admin"],
                'accessToken': "eyJhbGciOiJIUzUxMiJ9.admin",
                'refreshToken': "eyJhbGciOiJIUzUxMiJ9.adminRefresh",
                'expires': "2023/10/30 00:00:00"
            }
        }
    else:
        return {
            'success': True,
            'data': {
                'username': "common",
                'roles': ["common"],
                'accessToken': "eyJhbGciOiJIUzUxMiJ9.common",
                'refreshToken': "eyJhbGciOiJIUzUxMiJ9.commonRefresh",
                'expires': "2023/10/30 00:00:00"
            }
        }


@mock.get('/getAsyncRoutes')
async def get_router():
    permissionRouter = {
        'path': "/permission",
        'meta': {
            'title': "权限管理",
            'icon': "lollipop",
            'rank': 10
        },
        'children': [
            {
                'path': "/permission/page/index",
                'name': "PermissionPage",
                'meta': {
                    'title': "页面权限",
                    'roles': ["admin", "common"]
                }
            },
            {
                'path': "/permission/button/index",
                'name': "PermissionButton",
                'meta': {
                    'title': "按钮权限",
                    'roles': ["admin", "common"],
                    'auths': ["btn_add", "btn_edit", "btn_delete"]
                }
            }
        ]
    }

    creationRouter = {
        'path': "/creation",
        'meta': {
            'title': "创作",
            'icon': "lollipop",
            'rank': 10
        },
        'children': [
            {
                'path': "/creation/article/index",
                'name': "ArticlePage",
                'meta': {
                    'title': "文章管理",
                    'roles': ["admin", "common"]
                }
            },
            {
                'path': "/creation/tag/index",
                'name': "TagPage",
                'meta': {
                    'title': "标签管理",
                    'roles': ["admin", "common"]
                }
            }
        ]
    }

    logRouter = {
        'path': "/system",
        'meta': {
            'title': "系统管理",
            'icon': "lollipop",
            'rank': 10
        },
        'children': [
            {
                'path': '/system/log/index',
                'name': "LogPage",
                'meta': {
                    'title': "日志管理",
                    'roles': ["admin"],
                    'auths': ["btn_add", "btn_edit", "btn_delete"]
                }
            }
        ]
    }
    return {
        'success': True,
        'data': [permissionRouter, creationRouter, logRouter]
    }


@mock.post('/test')
async def test(body: dict):
    return {
        'success': True,
        'data': body
    }