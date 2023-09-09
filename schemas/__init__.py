from pydantic import BaseModel, Field
from datetime import date


class DateQueryParam(BaseModel):
    date_param: date = Field(..., description="Date parameter in yyyy-mm-dd format")
