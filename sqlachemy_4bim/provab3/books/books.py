from flask import Flask, render_template, url_for, request, Blueprint, redirect
from app.__init__ import User, Books
from auth.bp import auth_bp
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column



class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

bp = Blueprint('books', __name__, url_prefix='/books', template_folder='templates')

@bp.route('/')
@login_required
def index():
    return render_template('books/index.html', books =db.session.execute(db.select(Books).order_by(Books)).scalars())

@bp.route('/register', methods=['POST', 'GET'])
@login_required
def register():
    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']

        book = Books(
            titulo=request.form["titulo"],
            user=request.form["user"],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.index'))


    return render_template('books/register.html', users=db.session.execute(db.select(User).order_by(User)).scalars())