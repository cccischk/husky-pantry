import mysql.connector
from flask import current_app


#implement security stuff for the password and such
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='huskypantry_dev',
        password='BavWxQRiHfGK7nm',
        database='huskypantry_inventory'
    )




def add_user(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
