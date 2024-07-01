from typing import Optional

from pydantic import BaseModel, Field

from app.database import PyObjectId


class Item(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    description: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
