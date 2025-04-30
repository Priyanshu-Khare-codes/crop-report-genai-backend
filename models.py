from pydantic import BaseModel

class Report(BaseModel):
    crop_name: str
    crop_disease: str
    crop_disease_symptoms: list[str]
    crop_disease_cause: list[str]
    crop_disease_management: list[str]
    crop_disease_prevention: list[str]