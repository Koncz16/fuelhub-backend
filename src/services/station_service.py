from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.station_repository import StationRepository
from schemas.station import StationCreate, StationRead
from models.station_data import Station
from models.fuel_data import Fuel
from schemas.fuel import FuelCreate, FuelRead


class StationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_station(self, data: StationCreate) -> StationRead:

        station = await StationRepository.create(self.db, data)
        return StationRead.model_validate(station)

    async def create_station_with_fuel(self, data: StationCreate) -> StationRead:
        station = Station(
            external_id = data.external_id,
            name=data.name,
            brand=data.brand,
            city=data.city,
            county=data.county,
            address=data.address,
            postal_code=data.postal_code,
            latitude=data.latitude,
            longitude=data.longitude,
            fuels=[Fuel(**f.dict()) for f in data.fuels] if data.fuels else []
        )
        created_station = await StationRepository.create_with_fuel(self.db, station)
        return StationRead.model_validate(created_station)

    async def get_station(self, station_id: int) -> StationRead | None:
        station = await StationRepository.get(self.db, station_id)
        return StationRead.model_validate(station) if station else None

    async def get_fuel_by_station_id(self, station_id: int) -> List[FuelRead]:
        fuels = await StationRepository.get_fuel_by_station_id(self.db, station_id)
        return [FuelRead.model_validate(f) for f in fuels]    

    async def list_stations(self, skip: int = 0, limit: int = 100) -> list[StationRead]:
        stations = await StationRepository.list(self.db, skip, limit)
        return [StationRead.model_validate(s) for s in stations]
    
    async def list_stations_with_fuel(self, skip: int = 0, limit: int = 100) -> list[StationRead]:
        stations = await StationRepository.list_with_fuel(self.db, skip, limit)
        return [StationRead.model_validate(s) for s in stations]


    async def update_station(self, station_id: int, data: StationCreate) -> StationRead | None:
        station = await StationRepository.get(self.db, station_id)
        if not station:
            return None
        updated = await StationRepository.update(self.db, station, data)
        return StationRead.model_validate(updated)

    async def delete_station(self, station_id: int) -> bool:
        station = await StationRepository.get(self.db, station_id)
        if not station:
            return False
        await StationRepository.delete(self.db, station)
        return True
