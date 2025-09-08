from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SymptomLog(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)  # we'll store as string YYYY-MM-DD
    cycle_length = Column(Integer)
    acne = Column(String)
    mood = Column(String)
    weight = Column(Float)
