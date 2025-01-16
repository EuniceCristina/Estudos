from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    senha:Mapped[str]

class Livro(db.Model):
    __tablename___ = 'livros'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    editora:Mapped[str]

