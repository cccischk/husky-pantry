from flask import Flask, render_template
from models import get_db_connection

app = Flask( __name__)


@app.route('/')
def index():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SHOW DATABASES;")
        databases = [db[0] for db in cursor.fetchall()]
        out = "Databases: " + ", ".join(databases)
    except Exception as e:
        out = f"Database connection failed: {e}"
    finally:
        if 'db' in locals():
            db.close()
    return render_template('index.html', title='Home', output = out)

if __name__ == "__main__":
    app.run()