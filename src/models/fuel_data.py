from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FuelData(Base):
    __tablename__ = "fuel_data"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(String, nullable=False)
    fuel_type = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    city = Column(String, nullable=False)
    county = Column(String, nullable=False)
    address = Column(String, nullable=False)
    postal_code = Column(String, nullable=True)
