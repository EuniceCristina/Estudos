from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, relationship 
from sqlalchemy.orm import mapped_column, Mapped
from typing import List
from sqlalchemy import Table,Column, ForeignKey


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

usuarios_livros = Table(
    "usuarios_livros",
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('livros_id', ForeignKey('livros.id'), primary_key=True),
    
)

class User(db.Model):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    senha:Mapped[str]

    livros: Mapped[List['Livro']] = relationship(
        "Livro",
        secondary=usuarios_livros,
        back_populates="users"
    )
    

class Livro(db.Model):
    __tablename__ = 'livros'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    editora:Mapped[str]

    users: Mapped[List['User']] = relationship(
        "User",
        secondary=usuarios_livros,
        back_populates="livros"
    )


