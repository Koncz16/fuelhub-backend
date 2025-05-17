from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from schemas.station import StationCreate, StationRead, StationCreateWithFuel   
from schemas.fuel import FuelCreate, FuelRead
from services.station_service import StationService
from core.config import AsyncSessionLocal

router = APIRouter(prefix="/stations", tags=["Stations"])

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/", response_model=StationRead, status_code=status.HTTP_201_CREATED)
async def create_station(data: StationCreate, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    return await svc.create_station(data)

@router.post("/all", response_model=StationRead, status_code=status.HTTP_201_CREATED)
async def create_station_with_fuel(data: StationCreateWithFuel, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    return await svc.create_station_with_fuel(data)

@router.get("/", response_model=List[StationRead])
async def list_stations(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    return await svc.list_stations(skip, limit)


@router.get("/all", response_model=List[StationRead])
async def list_stations_with_fuel(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    return await svc.list_stations_with_fuel(skip, limit)


@router.get("/{station_id}", response_model=StationRead)
async def read_station(station_id: int, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    station = await svc.get_station(station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station

@router.get("/{station_id}/fuels", response_model=List[FuelRead])
async def get_station_fuels(station_id: int, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    return await svc.get_fuel_by_station_id(station_id)


@router.put("/{station_id}", response_model=StationRead)
async def update_station(station_id: int, data: StationCreate, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    updated = await svc.update_station(station_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Station not found")
    return updated

@router.delete("/{station_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_station(station_id: int, db: AsyncSession = Depends(get_db)):
    svc = StationService(db)
    success = await svc.delete_station(station_id)
    if not success:
        raise HTTPException(status_code=404, detail="Station not found")
    return


