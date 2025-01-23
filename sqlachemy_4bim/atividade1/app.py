from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import Table,Column, ForeignKey
from database.models import Student, Course, student_course_table

engine = create_engine('sqlite:///exemplo2.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

class Paciente(Base):
    __tablename__= 'pacientes'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    consultas:Mapped[List['Consulta']] = relationship(
        'Consulta', secondary=students_courses, 
    )