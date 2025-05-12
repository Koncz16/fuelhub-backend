from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from schemas.fuel import FuelDataCreate, FuelDataRead
from services import fuel_service
from core.config import AsyncSessionLocal

router = APIRouter(prefix="/fuel", tags=["Fuel"])

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/", response_model=FuelDataRead)
async def create_fuel_entry(data: FuelDataCreate, db: AsyncSession = Depends(get_db)):
    return await fuel_service.create_fuel(db, data)

@router.post("/bulk", response_model=List[FuelDataRead])
async def create_fuel_entries_bulk(data: List[FuelDataCreate], db: AsyncSession = Depends(get_db)):
    return await fuel_service.create_many_fuels(db, data)

@router.get("/", response_model=List[FuelDataRead])
async def list_fuel_entries(db: AsyncSession = Depends(get_db)):
    return await fuel_service.list_fuel(db)
