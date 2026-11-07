from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy

class Scientist(db.Model,SerializerMixin):
    __tablename__="scientists"

    serialize_rules=("-missions.scientist",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    field_of_study:Mapped[str]

    missions:Mapped[List["Mission"]]=relationship(back_populates="scientist",cascade="all,delete-orphan")
    planets=association_proxy("missions","planet",creator=lambda planet_obj:Mission(planet=planet_obj))


    def __repr__(self):

        return f"<Scientist {self.id}, {self.name}>"