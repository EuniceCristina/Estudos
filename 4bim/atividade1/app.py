from flask import Flask, render_template, request, url_for, redirect
from database.banco import Base,User,Livro, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        nome = request.form['nome']
        senha = request.form['senha']
        user = User(name=nome,senha=senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('livro'))
    return render_template('index.html')

@app.route('/livro', methods=['GET','POST'])
def livro():
    if request.method=='POST':
        nome = request.form['nome']
        editora = request.form['editora']
        livro = Livro(name=nome,editora=editora)
        db.session.add(livro)
        db.session.commit()
        return redirect(url_for('livro'))

   
    livros = Livro.query.all()
    return render_template('livro.html',livros=livros)