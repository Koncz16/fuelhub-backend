from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn

from api import api_router  

load_dotenv()

app = FastAPI(
    title="Fuel API",
    version=os.getenv("API_VERSION", "unknown")
)

app.include_router(api_router.router)


def main():    
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
