from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 

class Scientist(db.Model,SerializerMixin):
    __tablename__="scientists"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    field_of_study:Mapped[str]


    def __repr__(self):

        return f"<Scientist {self.id}, {self.name}>"