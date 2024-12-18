from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column , relationship
from database import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]

    livros = relationship("Livro", back_populates="user")

    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)


class Livro(db.Model):
    __tablename__ = 'livros'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # Relacionamento com usuários
    user = relationship("User", back_populates="livros")

    def __init__(self, nome, user_id) -> None:
        self.nome = nome
        self.user_id = user_id

