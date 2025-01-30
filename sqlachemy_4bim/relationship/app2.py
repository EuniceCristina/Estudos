from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

engine = create_engine('sqlite:///exemplo2.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

# Associative table for Many-to-Many relationship
estudante_curso = Table(
    "estudante_cursos",
    Base.metadata,
    Column('estudante_id', ForeignKey('estudantes.id'), primary_key=True),
    Column('curso_id', ForeignKey('cursos.id'), primary_key=True),
)

# Many-to-Many Relationship
class Curso(Base):
    __tablename__ = 'cursos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    
    # Correct Many-to-Many relationship
    estudantes: Mapped[List['Estudante']] = relationship(
        "Estudante",
        secondary=estudante_curso,
        back_populates="cursos"
    )

class Estudante(Base):
    __tablename__ = 'estudantes'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    
    # Correct Many-to-Many relationship
    cursos: Mapped[List[Curso]] = relationship(
        "Curso",
        secondary=estudante_curso,
        back_populates="estudantes"
    )

Base.metadata.create_all(bind=engine)

curso1=Curso(nome='Matemática')
curso2 = Curso(nome='Progamação')
estudante1=Estudante(nome='Alice')
estudante2=Estudante(nome='Bob')




# Associando cursos aos estudantes
estudante1.cursos.append(curso1)  # Alice faz Matemática
estudante1.cursos.append(curso2)  # Alice também faz Programação

estudante2.cursos.append(curso1)  # Bob faz Matemática

session.add_all([curso1,curso2,estudante1,estudante2])
session.commit()
