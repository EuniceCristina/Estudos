from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from core.models import User
from database import db

auth_bp = Blueprint(name="auth", 
    import_name=__name__, 
    url_prefix='/',
    template_folder='templates')

@auth_bp.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        senha = request.form['senha']
        nome = request.form['nome']

        # fazer a busca no banco pelo usuário pelo nome
        # Aqui você precisa de fato pegar o usuário no banco e logar ele
        user = db.session.execute(db.select(User).where(User.nome == nome)).first()
            
            
        if user[0] and user[0].senha == senha:
            login_user(user[0])
            return redirect(url_for('core.users'))
        else:
            return 'Deu não'
        
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        user = User(nome, email, senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
   

    return render_template('register.html')


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))