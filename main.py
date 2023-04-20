from core import create_app
from fastapi import FastAPI

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="localhost", port=8010, reload=True, lifespan="on")

