from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] 
    senha: Mapped[str]

    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha