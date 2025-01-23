from flask import Flask, request, render_template, \
    redirect, url_for, flash
import sqlite3, os.path
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models import User,Base, db

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()

# habilitar mensagens flash


# obtém conexão com o banco de dados


@app.route('/')
def index():
    users =User.query.all()
    return render_template('pages/index.html', users=users)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        senha= request.form['password']
        user = User(
            email=request.form["email"],
            senha=request.form["password"]
        )

        if not email:
            flash('Email é obrigatório')
        else:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('pages/create.html')

@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):

    # obter informação do usuário
    user = User.query.get(id)

    if user == None:
        return redirect(url_for('error', message='Usuário Inexistente'))

    if request.method == 'POST':
        email = request.form['email']

        user.email = email 
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('pages/edit.html', user=user)

@app.route('/error')
def error():
    error = request.args.get('message')
    return render_template('errors/error.html', message=error)