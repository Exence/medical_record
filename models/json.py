from pydantic import BaseModel


class JsonForm(BaseModel):
    json_data: dict