from sqlalchemy import Column, Integer,Table, String, Float, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

user_herbs = Table(
        "User_herbs",
        Base,
        Column("user_id", ForeignKey("User.user_id")),
        Column("Herb_ID", ForeignKey("Herb.Herb_ID"))
        )

class User(Base):
    __tablename__ = "User"
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    herbs: Mapped[list(Herb)] = relationship(secondary=user_herbs)
    org_id : Mapped[int] = mapped_column(ForeignKey("Organisation.organisation_id"))
    organisation: Mapped["Organisation"] = relationship(back_populates("users")
