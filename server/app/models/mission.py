from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 


class Mission(db.Model,SerializerMixin):
    __tablename__="missions"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]


    def __repr__(self):

        return f"<Mission {self.id}, {self.name}>"