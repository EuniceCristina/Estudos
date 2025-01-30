from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import Table,Column, ForeignKey

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

estudante_curso = Table(
    "estudante_cursos",
    Base.metadata,
    Column('estudantes_id', ForeignKey('estudantes.id'), primary_key=True),
    Column('cursos_id', ForeignKey('cursos.id'), primary_key=True),
)

# relacionamento NxN
class Curso(Base):
    __tablename__ = 'cursos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

class Estudante(Base):
    __tablename__ = 'estudantes'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
   

Base.metadata.create_all(bind=engine)
