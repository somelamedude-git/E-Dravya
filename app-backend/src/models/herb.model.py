from sqlalchemy import Column, Integer, String, Float, BigInteger, Boolean, CheckConstraint
from database import Base

class Herb(Base):
    __tablename__ = "Herb"
    Herb_Name = Column(String, unique=True)
    Herb_ID = Column(String, primary_key=True)
    Hydro_Tannins = Column(Boolean, default=False) # This means greenish-black, blue-black is given out in the test
    Condensed_Tannins = Column(Boolean, default=False) # This means the color green is given out in fecl3 test
    pH = Column(Float, CheckConstraint('pH>=0 AND pH<=14'))
    starch_present = Column(Boolean, default=False)
    conductivity = Column(Float)
    brix_score = Column(Float, CheckConstraint('brix_score>=0 AND brix_score <=100'))

