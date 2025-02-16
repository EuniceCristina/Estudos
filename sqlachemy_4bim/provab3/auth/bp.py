from flask import Blueprint, redirect, url_for, \
    request, render_template

from flask_login import LoginManager, login_required, login_user, logout_user
from app.__init__ import User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)

auth_bp = Blueprint(
    name='auth',
    import_name=__name__,
    template_folder='templates')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        users = db.session.execute(db.select(User).order_by(User.nome)).scalars()
        
        for user in users:
            if user['email'] == email:
                login_user(user)
                return redirect(url_for('users.index'))
        
    return render_template('auth/login.html')

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))