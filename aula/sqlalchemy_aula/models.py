from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, ForeignKey

from typing import List
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column(String(50), unique=True)
    my_receitas:Mapped[List['Receita']]=relationship('Receita', backref='user')


    def __repre__(self):
        return f"(User={self.nome})"

class Receita(Base):
    __tablename__ = 'receitas'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column(String(50), unique=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))


    def __repre__(self):
        return f"(Receita={self.nome})"
