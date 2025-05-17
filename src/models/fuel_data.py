from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.config import Base

class Fuel(Base):
    __tablename__ = "fuels"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  
    quality = Column(String, nullable=False)  
    price = Column(Float, nullable=False)  
    station_id = Column(Integer, ForeignKey("stations.id")) 

    station = relationship("Station", back_populates="fuels")
