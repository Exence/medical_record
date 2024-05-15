from pydantic import BaseModel, validator
from fastapi import HTTPException
from enum import Enum

from models.medical_record.child import Child


class AgeType(str, Enum):
  FIRST = "1-3 года"
  SECOND = "4-6 лет"
  THIRD = "Поступ. в 1 класс"

class AnnualReport(BaseModel):
  year: int
  age_type: AgeType
  children_count: int = 0
  frequently_abs: int = 0
  frequently_list: list[Child] = list()
  frequently_per: float = 0
  health_indx_abs: int = 0
  health_indx_list: list[Child] = list()
  health_indx_per: float = 0
  diseases_count_abs: int = 0
  diseases_count_on_thousand: float = 0
  missed_days_abs: int = 0
  missed_days_on_one: float = 0
  first_health_group: int = 0
  first_health_group_list: list[Child] = list()
  second_health_group: int = 0
  second_health_group_list: list[Child] = list()
  third_health_group: int = 0
  third_health_group_list: list[Child] = list()
  tub_positive: int = 0
  tub_positive_list: list[Child] = list()
  speech_defects: int = 0
  speech_defects_list: list[Child] = list()
  poor_posture: int = 0
  poor_posture_list: list[Child] = list()
  scoliosis: int = 0
  scoliosis_list: list[Child] = list()
  physical_development_disorders: int = 0
  physical_development_disorders_list: list[Child] = list()
  neurotic_disorders: int = 0
  neurotic_disorders_list: list[Child] = list()
  thinking_and_speech_disorders: int = 0
  thinking_and_speech_disorders_list: list[Child] = list()
  motor_development_disorders: int = 0
  motor_development_disorders_list: list[Child] = list()
  attention_and_memory_disorders: int = 0
  attention_and_memory_disorders_list: list[Child] = list()
  social_contacts_disorders: int = 0
  social_contacts_disorders_list: list[Child] = list()
  allergyes: int = 0
  allergyes_list: list[Child] = list()

  @validator('year')
  def check_year_range(cls, year):
        min_value = 2000
        max_value = 2100
        if not min_value <= year <= max_value:
            raise HTTPException(
                status_code=422, detail=f'Year must be between {min_value} and {max_value}')
        return year
