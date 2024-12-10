from flask import Flask, request, render_template, make_response, url_for, redirect

app = Flask(__name__)
resultado = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='GET':
        return render_template ('login.html')
    elif request.method=='POST':
        nome = request.form['nome']
        response = make_response(redirect(url_for('resultados')))
        response.set_cookie('nome',nome)
        return response

@app.route('/resultados',methods=['POST','GET'])
def resultados():
    nome = request.cookies.get('nome')
    texto = ''
    if request.method=='POST':
        distancia = request.form['distancia']
        tempo = request.form['tempo']
        resultado.append({'nome':nome,'distancia': distancia,'tempo':tempo})
        texto = 'Corrida registrada!'
    resultados = [res for res in resultado if res['nome'] == nome]
    return render_template('resultados.html',nome=nome,resultados=resultados,texto=texto)
    