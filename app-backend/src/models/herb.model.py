from sqlalchemy import Column, Integer, String, Float, BigInteger, Boolean, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Herb(Base):
    __tablename__ = "Herb"
    Herb_Name = Column(String, unique=True)
    Hydro_Tannins = Column(Integer, default=-1) # This means greenish-black, blue-black is given out in the test, the kind of hydrotannins also matter
    Condensed_Tannins = Column(Integer, default=-1) # This means the color green is given out in fecl3 test
    pH = Column(Float, CheckConstraint('pH>=0 AND pH<=14'))
    starch_present = Column(Integer, default=-1)
    conductivity = Column(Float)
    brix_score = Column(Float, CheckConstraint('brix_score>=0 AND brix_score <=100'))
    flavinoid_present = Column(Integer, default = -1)
    Taste = Column(String) # Taste spelling will probably always be right
    Confident_core_data = Column(Boolean, default= False)



