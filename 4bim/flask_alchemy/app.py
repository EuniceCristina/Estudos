from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int]= mapped_column(primary_key=True)
    nome:Mapped[str] 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'

# registrando no sqlalchmey a app
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    user1 = User(nome = 'pudim')

    db.session.add(user1)
    db.session.commit()
    return render_template('index.html')

@app.route('/listar')
def listar():
    sttm = db.select(User)
    resultado = db.session.execute(sttm).scalars()
    #resultado = db.session.query(User).scalars()
    return render_template('listar.html', resultado=resultado)