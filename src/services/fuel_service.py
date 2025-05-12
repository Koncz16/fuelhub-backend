from sqlalchemy.ext.asyncio import AsyncSession
from schemas.fuel import FuelDataCreate
from repositories import fuel_repository


async def create_fuel(db: AsyncSession, data: FuelDataCreate):
    return await fuel_repository.create_fuel_data(db, data)

async def create_many_fuels(db: AsyncSession, data: list[FuelDataCreate]):
    return await fuel_repository.create_many_fuel_data(db, data)

async def list_fuel(db: AsyncSession):
    return await fuel_repository.get_all_fuel_data(db)
