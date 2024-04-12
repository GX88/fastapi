import typer
from core import create_app
from application import config as f

app = create_app()
shell_app = typer.Typer()


@shell_app.command()
def run(
        host: str = typer.Option(default=f.APP_HOST, help='监听主机IP，默认开放给本网络所有主机'),
        port: int = typer.Option(default=f.APP_PORT, help='监听端口'),
        reload: bool = typer.Option(default=f.APP_RELOAD, help='是否开启热更新')
):
    import uvicorn

    uvicorn.run(
        app='main:app',
        host=host,
        port=port,
        reload=reload,
    )


if __name__ == '__main__':
    shell_app()
