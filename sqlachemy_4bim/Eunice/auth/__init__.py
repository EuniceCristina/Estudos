from flask_login import LoginManager
from core.models import User
from database import db

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)