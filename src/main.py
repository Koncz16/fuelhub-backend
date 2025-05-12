from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn

from api import api_router, fuel_router
from core.config import engine
from models.fuel_data import Base

load_dotenv()

app = FastAPI(
    title="Fuel API",
    version=os.getenv("API_VERSION", "unknown")
)

app.include_router(api_router.router)
app.include_router(fuel_router.router)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def main():    
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
