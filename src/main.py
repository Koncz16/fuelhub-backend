from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn

from api import api_router, fuel_router, station_router
from core.config import engine, Base
from models.station_data import Station

load_dotenv()

app = FastAPI(
    title="Fuel API",
    version=os.getenv("API_VERSION", "unknown")
)

app.include_router(api_router.router)
app.include_router(fuel_router.router)
app.include_router(station_router.router)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def main():    
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
