from flask import Flask, render_template, request, url_for, redirect, session
from database.banco import Base,User,Livro, db, usuarios_livros

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()

app.secret_key = 'chave_super_secreta' 


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        
        # Criar usuário e salvar no banco
        user = User(name=nome, senha=senha)
        db.session.add(user)
        db.session.commit()
        
        # Salvar ID do usuário na sessão
        session['user_id'] = user.id  

        return redirect(url_for('livro'))
    
    return render_template('index.html')

@app.route('/livro', methods=['GET', 'POST'])
def livro():
    user_id = session.get('user_id')  # Obtém ID do usuário logado

    if not user_id:
        return redirect(url_for('index'))  # Redireciona se não estiver logado

    user = User.query.get(user_id)  # Busca o objeto User

    if request.method == 'POST':
        nome = request.form['nome']
        editora = request.form['editora']

        livro = Livro(name=nome, editora=editora)

        # Associa o livro ao usuário
        user.livros.append(livro)

        db.session.add(livro)
        db.session.commit()

        return redirect(url_for('livro'))

    livros = Livro.query.all()
    return render_template('livro.html', livros=livros, user=user)


   
    
