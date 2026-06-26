from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def create_database():
    conn = sqlite3.connect("person.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email VARCHAR(255),
        phone VARCHAR(20),
        city VARCHAR(100),
        country VARCHAR(100)
    )
    """)

    conn.commit()
    conn.close()
    print("Database created")

def insert_data():
    conn = sqlite3.connect("person.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users
    (first_name, last_name, email, phone, city, country)
    VALUES (A,B,abc@gmail.com,1234567890,Ha Noi,Vietnam)
    """)
    conn.commit()
    conn.close()
    print("Data inserted")

def getData():
    conn = sqlite3.connect("person.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    output = cursor.fetchall()
    conn.close()
    return output

@app.route("/", methods=["GET"])
def home():
    return "hello world"

@app.route("/get_person_information", methods=["GET"])
def get_person_information():
    data = getData()
    return jsonify(data)

@app.route("/create_person", methods=["POST"])
def create_person():

    request_data = request.get_json()

    conn = sqlite3.connect("person.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (first_name, last_name, email, phone, city, country)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        request_data["first_name"],
        request_data["last_name"],
        request_data["email"],
        request_data["phone"],
        request_data["city"],
        request_data["country"]
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Person created successfully!"
    })

if __name__ == "__main__":
    app.run(debug=True)