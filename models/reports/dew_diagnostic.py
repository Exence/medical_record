from datetime import date
from pydantic import BaseModel


class DewDiagnostic(BaseModel):
    start_date: date
    end_date: date
    absolute: int
    positive_count: int
    negative_count: int