from core import create_app
import config as f

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app='main:app',
        host=f.APP_HOST,
        port=f.APP_PORT,
        reload=f.APP_RELOAD
    )

