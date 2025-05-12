from pydantic import BaseModel

class FuelDataCreate(BaseModel):
    price: str
    fuel_type: str
    brand: str 
    city: str
    county: str
    address: str
    postal_code: str

class FuelDataRead(FuelDataCreate):
    id: int

    class Config:
        orm_mode = True
