from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_manager, login_user, logout_user, login_required, current_user
from database import db
from models.models import User, Livro


app = Flask(__name__)
app.config['SECRET_KEY'] = 'muitodificil'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

login_manager.login_view = 'login'  # Define a página de login
login_manager.login_message = "Por favor, faça login para acessar esta página."

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        senha = request.form['senha']
        user = db.session.execute(db.select(User).where(User.email == email)).first()
        
        
        if user[0] and check_password_hash(user[0].senha, senha):
            login_user(user[0])
            return redirect(url_for('livros'))
        else:
            return 'Deu não'


    return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        user = User(nome,email,senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


    return render_template('register.html')

@app.route("/livros", methods=['GET','POST'])
@login_required
def livros():
    if request.method == 'POST':
        nome = request.form['nome']
        if not nome:  
            flash("O nome do livro é obrigatório.", "danger")
            return redirect(url_for('livros'))

        
        livro = Livro(nome=nome, user_id=current_user.id)
        db.session.add(livro)
        db.session.commit()
        flash("Livro adicionado com sucesso!", "success")
        return redirect(url_for('livros'))
   
    livros= db.session.execute(
        db.select(Livro).where(Livro.user_id == current_user.id)
    ).scalars().all()
    
    return render_template('livros.html', livros=livros)

if __name__ == "__main__":
    app.run(debug=True)