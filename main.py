from fastapi import FastAPI
import uvicorn
from settings import settings
from api import router


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.server_host, port=settings.server_port, reload=True)