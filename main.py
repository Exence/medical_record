import uvicorn
import locale

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from settings import settings
from app import router as app_router
from api import router as api_router


locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
app = FastAPI(
    redoc_url=None,
    )
app.include_router(app_router, include_in_schema=False)
app.include_router(api_router)

app.mount('/static', StaticFiles(directory='static'), name='static')

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.server_host, port=settings.server_port, reload=True)