from datetime import date
from pydantic import BaseModel


class TubDiagnostic(BaseModel):
    start_date: date
    end_date: date
    absolute: int
    positive_count: int
    doubtful_count: int
    negative_count: int