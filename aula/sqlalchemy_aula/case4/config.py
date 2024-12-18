from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base,User
from faker import Faker

engine = create_engine('sqlite:///test.db')
session = Session(bind=engine)

def start_db():
    Base.metadata.create_all(bind=engine)
    gerador_lero = Faker()

    for i in range(10):
        nome_fake = gerador_lero.unique.name()
        user = User(nome=nome_fake)
        session.add(user)

    session.commit()
    
   

def destroy_db():
    Base.metadata.drop_all(bind=engine)