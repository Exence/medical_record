from starlette.templating import Jinja2Templates
from pathlib import Path


current_dir = Path(__file__)
templates = Jinja2Templates(directory=current_dir.parents[1] / "templates")