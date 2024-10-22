from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="user",
        password="password"
    )
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

