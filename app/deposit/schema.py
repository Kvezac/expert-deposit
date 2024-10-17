from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from app.config import settings
from app.exceptions import InputDateError


class DepositCreationSchema(BaseModel):
    date: str = Field(..., description="Date in format 'dd.mm.YYYY'", examples=['24.08.2024'])
    periods: int = Field(ge=1, le=60, description="Periods deposit", examples=['10'])
    amount: int = Field(ge=10000, le=3000000, description="Amount deposit", examples=['10000'])
    rate: float = Field(ge=1, le=8, description="Interest rate deposit", examples=['4.5'])

    @field_validator('date')
    def is_data(self, value) -> date | ValueError:
        try:
            datetime.strptime(value, settings.DATE_FOMAT).date()
        except InputDateError as e:
            raise ValueError(f"error: {e.detail} {settings.DATE_FORMAT} {e.status_code}")
        return value


class DepositSchema(DepositCreationSchema):
    id: int

    class Config:
        from_attributes = True
