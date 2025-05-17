from sqlalchemy.ext.asyncio import AsyncSession
from repositories.fuel_repository import FuelRepository
from schemas.fuel import FuelCreate, FuelRead

class FuelService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_fuel(self, data: FuelCreate) -> FuelRead:
        fuel = await FuelRepository.create(self.db, data)
        return FuelRead.model_validate(fuel)

    async def get_fuel(self, fuel_id: int) -> FuelRead | None:
        fuel = await FuelRepository.get(self.db, fuel_id)
        return FuelRead.model_validate(fuel) if fuel else None

    async def list_fuels(self, skip: int = 0, limit: int = 100) -> list[FuelRead]:
        fuels = await FuelRepository.list(self.db, skip, limit)
        return [FuelRead.model_validate(f) for f in fuels]

    async def update_fuel(self, fuel_id: int, data: FuelCreate) -> FuelRead | None:
        fuel = await FuelRepository.get(self.db, fuel_id)
        if not fuel:
            return None
        updated = await FuelRepository.update(self.db, fuel, data)
        return FuelRead.model_validate(updated)

    async def delete_fuel(self, fuel_id: int) -> bool:
        fuel = await FuelRepository.get(self.db, fuel_id)
        if not fuel:
            return False
        await FuelRepository.delete(self.db, fuel)
        return True
