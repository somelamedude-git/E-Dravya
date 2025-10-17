from sqlalchemy import Column, Integer, String, Float, BigInteger
from database import Base

class User(Base):
    __tablename__ = "User"
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    user_id = Column(Integer, primary_key=True)
