from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy

class Planet(db.Model,SerializerMixin):
    __tablename__="planets"

    serialize_rules=("-missions.planet",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    distance_from_earth:Mapped[int]
    nearest_star:Mapped[str]

    missions:Mapped[List["Mission"]]=relationship(back_populates="planet",cascade="all,delete-orphan")
    scientists=association_proxy("missions","scientist",creator=lambda scientist_obj:Mission(scientist=scientist_obj))



    def __repr__(self):

        return f"<Planet {self.id}, {self.name}>"