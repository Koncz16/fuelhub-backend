from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.station_data import Station
from schemas.station import StationCreate
from models.fuel_data import Fuel
from sqlalchemy.future import select
from sqlalchemy.orm import noload

class StationRepository:
    @staticmethod
    async def create(db: AsyncSession, data: StationCreate) -> Station:
        station = Station(**data.dict())
        db.add(station)
        await db.commit()
        await db.refresh(station)
        return station

    @staticmethod
    async def create_with_fuel(db: AsyncSession, station: Station) -> Station:
        db.add(station)
        await db.commit()
        await db.refresh(station)
        return station


    @staticmethod
    async def get(db: AsyncSession, station_id: int) -> Station | None:
        result = await db.execute(select(Station).where(Station.id == station_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_fuel_by_station_id(db: AsyncSession, station_id: int) -> List[Fuel]:
        result = await db.execute(select(Fuel).where(Fuel.station_id == station_id))
        return result.scalars().all()

    @staticmethod
    async def list(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Station]:
        result = await db.execute(select(Station).options(noload(Station.fuels)).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def list_with_fuel(db: AsyncSession, skip: int = 0, limit: int = 100 ) -> List[Station]:
        result = await db.execute(select(Station).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def update(db: AsyncSession, station: Station, data: StationCreate) -> Station:
        for field, val in data.dict().items():
            setattr(station, field, val)
        await db.commit()
        await db.refresh(station)
        return station

    @staticmethod
    async def delete(db: AsyncSession, station: Station) -> None:
        await db.delete(station)
        await db.commit()

