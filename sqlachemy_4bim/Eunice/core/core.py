from flask import Blueprint, render_template
from flask_login import login_required
from core.models import User
from database import db

core = Blueprint(name="core", 
    import_name=__name__, 
    url_prefix='/core',
    template_folder='templates')



@core.route('/users', methods=['POST', 'GET'])
@login_required
def users():
    #user = db.select(User).all()
    users = db.session.execute(db.select(User)).scalars().all()
    return render_template('core/users.html', users=users)
