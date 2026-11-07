from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 

class Planet(db.Model,SerializerMixin):
    __tablename__="planets"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    distance_from_earth:Mapped[int]
    nearest_star:Mapped[str]



    def __repr__(self):

        return f"<Planet {self.id}, {self.name}>"