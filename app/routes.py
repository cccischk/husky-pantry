from flask import Blueprint, render_template
from app.models import get_db_connection

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE test_db;")
    cursor.execute("SHOW DATABASES;")
    out = "These are the dbs: "
    for db in cursor.fetchall():
        out += (db)

    return render_template('index.html', title='Home', output = out)
