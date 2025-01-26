from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_FILE = "users.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


init_db()


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify({"message": "Name and age are required"}), 400

    if 10 < age < 18:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
        conn.close()

        return jsonify({"message": f"Welcome {name}, you are eligible!"}), 200
    else:
        return jsonify({"message": "You are not eligible"}), 400


if __name__ == '__main__':
    app.run(debug=True)
