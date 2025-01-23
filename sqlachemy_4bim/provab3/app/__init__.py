from flask import Flask, render_template
from users import users
from books import books
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column



class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


# importar auth_bluprint e login_manager (PROVA)
from auth.bp import auth_bp, login_manager

app = Flask (__name__, template_folder='templates')

# secret key (PROVA)
app.config['SECRET_KEY'] = 'SENHASENHASENHA'
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column()
    

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]


with app.app_context():
    db.create_all()

#Inicializar app no login_manage (prova)
login_manager.init_app(app)

# registrar blueprint
app.register_blueprint(auth_bp)

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)


@app.route('/')
def index():
    return render_template('layout.html')