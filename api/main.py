from fastapi import APIRouter
from starlette.requests import Request

from .template_path import templates


router = APIRouter(
    tags=['Main page']
)

@router.get('/')
async def main(request: Request):
    return templates.TemplateResponse('login_page/index.html', {'request': request})