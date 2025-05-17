from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.fuel_data import Fuel
from schemas.fuel import FuelCreate


class FuelRepository:
    @staticmethod
    async def create(db: AsyncSession, fuel_in: FuelCreate) -> Fuel:
        fuel = Fuel(**fuel_in.dict())
        db.add(fuel)
        await db.commit()
        await db.refresh(fuel)
        return fuel

    @staticmethod
    async def get(db: AsyncSession, fuel_id: int) -> Fuel | None:
        result = await db.execute(select(Fuel).where(Fuel.id == fuel_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def list(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Fuel]:
        result = await db.execute(select(Fuel).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def update(db: AsyncSession, fuel: Fuel, fuel_in: FuelCreate) -> Fuel:
        for field, value in fuel_in.dict().items():
            setattr(fuel, field, value)
        await db.commit()
        await db.refresh(fuel)
        return fuel

    @staticmethod
    async def delete(db: AsyncSession, fuel: Fuel) -> None:
        await db.delete(fuel)
        await db.commit()