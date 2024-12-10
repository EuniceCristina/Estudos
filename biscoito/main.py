from flask import Flask, render_template
from flask import request, make_response, url_for

app= Flask(__name__)

@app.route('/')
def index():
    cor = 'white'
    if 'color' in request.cookies:
        cor = request.cookies['color']
    return render_template('index.html',cor=cor)

@app.route('/color', methods=['GET','POST'])
def color():
    cor = request.form['color']

    #preparação da resposta a cliente
    template = render_template('color.html', cor=cor)
    response = make_response(template)

    #garante que alteração do cookie aconteça
    if 'color' in request.cookies and cor != request.cookies['color']:
        response.delete_cookie('color')
    
    response.set_cookie('color', value=cor)

    return response