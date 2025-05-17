from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from core.config import Base

class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False) 
    brand = Column(String, nullable=True)  
    city = Column(String, nullable=False)  
    county = Column(String, nullable=False)  
    address = Column(String, nullable=False)  
    postal_code = Column(String, nullable=True)  
    latitude = Column(Float, nullable=False)  
    longitude = Column(Float, nullable=False)  
    
    fuels = relationship(
    "Fuel",
    back_populates="station",
    cascade="all, delete",
    lazy="selectin"
    )
