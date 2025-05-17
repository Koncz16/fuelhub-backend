from pydantic import BaseModel

class FuelCreate(BaseModel):
    type: str
    quality: str
    price: float

class FuelRead(FuelCreate):
    id: int
    
    class Config:
        from_attributes = True  