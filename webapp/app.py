import os
import time
from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASS = os.getenv('DB_PASS', '')
DB_NAME = os.getenv('DB_NAME', 'test')

def get_db_connection(retries=10, delay=2):
    for attempt in range(1, retries+1):
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                database=DB_NAME
            )
            return conn
        except Exception as e:
            print(f"[db connect] attempt {attempt}/{retries} failed: {e}")
            time.sleep(delay)
    raise Exception("Could not connect to DB after retries")

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
      CREATE TABLE IF NOT EXISTS visits (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    """)
    cur.execute("INSERT INTO visits () VALUES ()")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"Hello! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
