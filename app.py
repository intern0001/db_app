# app.py
from flask import Flask, render_template, request
import os
import psycopg2

app = Flask(__name__)

# Use environment variables for database credentials
db_credentials = {
    'dbname': os.environ.get('POSTGRES_DATABASE'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'host': os.environ.get('POSTGRES_HOST'),
    'port': os.environ.get('POSTGRES_PORT')
}

@app.route('/')
def index():
    try:
        connection = psycopg2.connect(**db_credentials)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        data = cursor.fetchall()
        connection.close()
        return render_template('index.html', data=data)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
