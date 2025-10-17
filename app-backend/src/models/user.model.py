from sqlalchemy import Column, Integer, String, Float, BigInteger
from database import Base

class User(Base):
    __tablename__ = "User"
    username = Column(String)
    email = Column(String, primary_key=True)
    password = Column(String)

