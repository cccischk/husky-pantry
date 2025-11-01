import mysql.connector
from flask import current_app

def get_db_connection():
    return mysql.connector.connect(
        host=current_app.config['localhost'],
        user=current_app.config['huskypantry_dev'],
        password=current_app.config['BavWxQRiHfGK7nm'],
        database=current_app.config['huskypantry_inventory']
    )




def add_user(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
