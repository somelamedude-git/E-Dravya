from sqlalchemy import Column, Integer, String, Float, Boolean, CheckConstraint, Table, ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

organisation_herbs = Table(
        "organisation_herbs",
        Base,
        Column("org_id", ForeignKey("Organisation.organisation_id")),
        Column("herb_id", ForeignKey("Herb.Herb_ID"))
        )

class Organisation(Base):
    __tablename__ = "Organisation"
    organisation_id:Mapped[int] = mapped_column(primary_key=True)
    organisation_name = Column(String)
    herbs:Mapped[list[Herb]] = relationship(secondary=organisation_herbs)
    users: Mapped[list("User")] = relationship(back_populates="organisation")


