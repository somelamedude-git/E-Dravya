from sqlalchemy import Column, Integer, String, Float, Boolean, CheckConstraint, Table, ForeignKey
from database import Base

organisation_herbs = Table(
        "organisation_herbs",
        Base,
        Column("org_id", ForeignKey("Organisation.organisation_id")),
        Column("herb_id", ForeignKey("Herb.Herb_ID"))
        )

class Organisation(Base):
    __tablename__ = "Organisation"
    organisation_id = Column(Integer, primary_key=True)
    organisation_name = Column(String)

