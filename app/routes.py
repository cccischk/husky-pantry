from flask import Blueprint, render_template
from models import get_db_connection

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor()
    return render_template('index.html', title='Home')