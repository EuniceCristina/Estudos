from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# classe definida em models.py - 
from models import Base, User

# carregar variáveis de ambiente
load_dotenv()

# utilizado para fabricar dados 


# criar conexão com banco
engine = create_engine(os.getenv('SQLITE'))

# A classe base utiliza os metadados dos modelos para 
# criar a estrutura no banco de dados
Base.metadata.create_all(bind=engine)

# Cria sessão para manipulação do banco
session = Session(bind=engine)

# criação e adição de 10 usuários ao banco
@app.route('/')
def index():
    users = session.query(User).all()
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        nome = request.form['nome']

        user = User(nome=nome)
        session.add(user)
        session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

    
session.commit ()
