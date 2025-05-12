from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.fuel_data import FuelData
from schemas.fuel import FuelDataCreate


async def create_fuel_data(db: AsyncSession, fuel: FuelDataCreate) -> FuelData:
    new_fuel = FuelData(**fuel.model_dump())
    db.add(new_fuel)
    await db.commit()
    await db.refresh(new_fuel)
    return new_fuel


async def create_many_fuel_data(db: AsyncSession, fuels: list[FuelDataCreate]) -> list[FuelData]:
    fuel_objects = [FuelData(**fuel.model_dump()) for fuel in fuels]
    db.add_all(fuel_objects)
    await db.commit()
    for fuel in fuel_objects:
        await db.refresh(fuel)
    return fuel_objects


async def get_all_fuel_data(db: AsyncSession) -> list[FuelData]:
    result = await db.execute(select(FuelData))
    return result.scalars().all()
