from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from schemas.fuel import FuelCreate, FuelRead
from services.fuel_service import FuelService
from core.config import AsyncSessionLocal  # your session factory

router = APIRouter(prefix="/fuels", tags=["Fuels"])

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/", response_model=FuelRead, status_code=status.HTTP_201_CREATED)
async def create_fuel(data: FuelCreate, db: AsyncSession = Depends(get_db)):
    svc = FuelService(db)
    return await svc.create_fuel(data)

@router.get("/{fuel_id}", response_model=FuelRead)
async def read_fuel(fuel_id: int, db: AsyncSession = Depends(get_db)):
    svc = FuelService(db)
    fuel = await svc.get_fuel(fuel_id)
    if not fuel:
        raise HTTPException(status_code=404, detail="Fuel not found")
    return fuel

@router.get("/", response_model=List[FuelRead])
async def list_fuels(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    svc = FuelService(db)
    return await svc.list_fuels(skip, limit)

@router.put("/{fuel_id}", response_model=FuelRead)
async def update_fuel(fuel_id: int, data: FuelCreate, db: AsyncSession = Depends(get_db)):
    svc = FuelService(db)
    updated = await svc.update_fuel(fuel_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Fuel not found")
    return updated

@router.delete("/{fuel_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fuel(fuel_id: int, db: AsyncSession = Depends(get_db)):
    svc = FuelService(db)
    success = await svc.delete_fuel(fuel_id)
    if not success:
        raise HTTPException(status_code=404, detail="Fuel not found")
    return
