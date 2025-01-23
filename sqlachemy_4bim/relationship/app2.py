from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import Table,Column, ForeignKey

engine = create_engine('sqlite:///exemplo2.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

estudante_curso = Table(
    "estudante_cursos",
    Base.metadata,
    Column('estudante_id', ForeignKey('estudantes.id'), primary_key=True),
    Column('curso_id', ForeignKey('curso.id'), primary_key=True),
)

# relacionamento NxN
class Curso(Base):
    __tablename__ = 'cursos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    estudantes:Mapped[List['Estudante']] = relationship('Estudante', backref='curso')

class Estudante(Base):
    __tablename__ = 'Estudante'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    curso_id = mapped_column(
        ForeignKey('cursos.id'), nullable=True
    )

Base.metadata.create_all(bind=engine)

info = Curso(nome='Informática')
session.add(info)

x = Estudante(nome='Mané Cabelim')
y = Estudante(nome='Zuca')
z = Estudante(nome='Novim')
session.add_all([y,x,z])
session.commit()