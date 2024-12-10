from flask import Flask, request, render_template, url_for, make_response, redirect

app = Flask(__name__)


corridas=[]
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        nome = request.form['nome']
        resp = make_response(redirect(url_for('corrida')))
        resp.set_cookie('nome', nome)
        return resp
    return render_template('login.html')

@app.route('/corrida', methods=['GET','POST'])
def corrida():
    nome = request.cookies.get('nome')
    if request.method=='POST':
        distancia = request.form['distancia']
        tempo = request.form['tempo']
        corridas.append({"nome": nome, "distancia": distancia, "tempo": tempo})
        
    user_corridas= [m for m in corridas if m['nome'] == nome]
    return render_template('corrida.html', nome=nome, user_corridas=user_corridas)


