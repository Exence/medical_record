from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from settings import settings
from api import router


app = FastAPI(
    redoc_url=None,
    )
app.include_router(router)
app.mount('/static', StaticFiles(directory='static'), name='static')

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.server_host, port=settings.server_port, reload=True)