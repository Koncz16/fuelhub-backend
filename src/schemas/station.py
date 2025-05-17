from pydantic import BaseModel
from typing import List, Optional
from schemas.fuel import FuelCreate, FuelRead

class StationCreate(BaseModel):
    external_id: int
    name: str
    brand: Optional[str]
    city: str
    county: str
    address: str
    postal_code: Optional[str]
    latitude: float
    longitude: float


class StationCreateWithFuel(StationCreate):
    fuels: Optional[List[FuelCreate]] = []


class StationRead(StationCreate):
    id: int
    fuels: List[FuelRead] = []

    class Config:
        from_attributes = True  # Pydantic V2
