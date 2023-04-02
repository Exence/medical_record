from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates(directory="templates")


router = APIRouter(
    tags=['Main page']
)
 
@router.get('/')
async def main(request: Request):
    return templates.TemplateResponse('login_page/index.html', {'request': request})