from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 
from sqlalchemy import ForeignKey


class Mission(db.Model,SerializerMixin):
    __tablename__="missions"

    serialize_rules=("-scientist.missions","-planet.missions",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

    scientist_id:Mapped[int]=mapped_column(ForeignKey("scientists.id"))
    planet_id:Mapped[int]=mapped_column(ForeignKey("planets.id"))

    scientist:Mapped["Scientist"]=relationship(back_populates="missions")
    planet:Mapped["Planet"]=relationship(back_populates="missions")


    def __repr__(self):

        return f"<Mission {self.id}, {self.name}>"