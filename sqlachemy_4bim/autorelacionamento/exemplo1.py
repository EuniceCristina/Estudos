from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import select
from typing import List

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    gerente_id = mapped_column(ForeignKey('users.id'), nullable=True)

    gerenciados:Mapped[List['User']] = relationship('User', back_populates='gerente')
    gerente = relationship('User', back_populates='gerenciados', remote_side=[id])

    def __repr__(self) -> str:
        return self.nome



Base.metadata.create_all(bind=engine)

#user1 = User(nome='Duca')

#session.add(user1)
#session.commit()

#user2 = User(nome='Machado de Assis', gerente_id=1)
#user3 = User(nome='Zubé', gerente_id=1)
#user4 = User(nome='Miga')
#user5 = User(nome='Hermenegildo')

#session.add_all([user2,user3,user4,user5])
#session.commit()

sttm = select(User).where(User.id == 1)
print(sttm)

chefe = session.execute(sttm).scalars().first()
print('-----> ',chefe.nome)
print('-----> ',chefe.gerenciados)


sttm = select(User).where(User.id == 2)
pessoa = session.execute(sttm).scalars().first()
print('Eu sou: ' + str(pessoa))
print('MEu chefe é: ' + str(pessoa.gerente))