from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///florista.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rg = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

# Modelo Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)

# Modelo Pedido
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id', ondelete="CASCADE"), nullable=False)
    data_pedido = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    produtos = db.relationship('PedidoProduto', backref='pedido', cascade="all, delete", lazy=True)

# Modelo de Associação Pedido-Produto (Relacionamento N:N)
class PedidoProduto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id', ondelete="CASCADE"), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id', ondelete="CASCADE"), nullable=False)
    
    # ✅ Adicionando relacionamento para acessar o produto corretamente
    produto = db.relationship('Produto', backref='pedido_produto')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    clientes = Cliente.query.all()
    return render_template('cliente.html', clientes=clientes)

@app.route('/produtos')
def produtos():
    produtos = Produto.query.all()
    return render_template('produto.html', produtos=produtos)

@app.route('/pedidos')
def pedidos():
    pedidos = Pedido.query.all()
    clientes = Cliente.query.all()
    produtos = Produto.query.all()
    return render_template('pedido.html', pedidos=pedidos, clientes=clientes, produtos=produtos)

@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    rg = request.form['rg']
    nome = request.form['nome']
    telefone = request.form['telefone']
    novo_cliente = Cliente(rg=rg, nome=nome, telefone=telefone)
    db.session.add(novo_cliente)
    db.session.commit()
    return redirect(url_for('clientes'))

@app.route('/add_produto', methods=['POST'])
def add_produto():
    nome = request.form['nome']
    tipo = request.form['tipo']
    preco = request.form['preco']
    novo_produto = Produto(nome=nome, tipo=tipo, preco=preco)
    db.session.add(novo_produto)
    db.session.commit()
    return redirect(url_for('produtos'))

@app.route('/add_pedido', methods=['POST'])
def add_pedido():
    cliente_id = request.form['cliente_id']
    produtos_ids = request.form.getlist('produtos')
    novo_pedido = Pedido(cliente_id=cliente_id)
    db.session.add(novo_pedido)
    db.session.commit()

    for produto_id in produtos_ids:
        novo_pedido_produto = PedidoProduto(pedido_id=novo_pedido.id, produto_id=produto_id)
        db.session.add(novo_pedido_produto)

    db.session.commit()
    return redirect(url_for('pedidos'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
