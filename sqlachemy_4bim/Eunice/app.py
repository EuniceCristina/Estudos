from core.core import core
from auth import login_manager
from auth.routes import auth_bp
from flask import Flask
from database import db

# importar Base e engine

# Inicializa a apliacação
application = Flask(__name__)
application.config['SECRET_KEY'] = '123123123123'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

# crair o banco com Base.medatada.create_all()

# Inicializa o controle de sessões
db.init_app(application)
login_manager.init_app(application)

# Registra as rotas da aplicação
application.register_blueprint(core)

# Registra rotas de login/logout
application.register_blueprint(auth_bp)

with application.app_context():
    db.create_all()


