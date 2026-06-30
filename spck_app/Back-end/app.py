from flask import Flask, jsonify, request
from flask_cors import CORS

import re
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Game Collection Manager"

@app.route("/games/<int:user_id>", methods=["GET"])
def get_games(user_id):

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM games WHERE user_id=?",
        (user_id,)
    )

    games = cursor.fetchall()

    conn.close()

    return jsonify(games)

@app.route("/games", methods=["POST"])
def add_game():
    request_data = request.get_json()
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO games
    (user_id, name, genre, hours_played, status)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        request_data["user_id"],
        request_data["name"],
        request_data["genre"],
        request_data["hours_played"],
        request_data["status"]
    ))
    conn.commit()
    conn.close()
    return jsonify({
        "message":"Game Added"
    })

@app.route("/games/<int:id>", methods=["DELETE"])
def delete_game(id):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM games WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({
        "message":"Game Deleted"
    })

@app.route("/games/<int:id>", methods=["PUT"])
def update_game(id):
    request_data=request.get_json()
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE games
        SET hours_played=?
        WHERE id=?
        """, 
        (
            request_data["hours_played"], 
            id
        )
    )
    conn.commit()
    conn.close()
    return jsonify({
        "message":"Game Updated"
    })

@app.route("/stats", methods=["GET"])
def stats():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM games")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM games WHERE status='Playing'")
    playing = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM games WHERE status='Completed'")
    completed = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM games WHERE status='Wishlist'")
    wishlist = cursor.fetchone()[0]
    conn.close()
    return jsonify({
        "total":total,
        "playing":playing,
        "completed":completed,
        "wishlist":wishlist
    })

@app.route("/search/<name>")
def search(name):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM games WHERE name LIKE ?",
        ("%" + name + "%",)
    )
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route("/register", methods=["POST"])
def register():
    request_data = request.get_json()
    first_name = request_data["first_name"].strip()
    last_name = request_data["last_name"].strip()
    email = request_data["email"].strip()
    password = request_data["password"]
    if first_name == "":
        return jsonify({"success":False,"message":"First Name is required."})
    if last_name == "":
        return jsonify({"success":False,"message":"Last Name is required."})
    if email == "":
        return jsonify({"success":False,"message":"Email is required."})
    if password == "":
        return jsonify({"success":False,"message":"Password is required."})

    email_pattern = r'^[^@]+@[^@]+\.[^@]+$'

    if not re.match(email_pattern,email):
        return jsonify({"success":False,"message":"Invalid email."})

    if len(password) < 8:
        return jsonify({"success":False,"message":"Password must be at least 8 characters."})

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    if cursor.fetchone():
        conn.close()
        return jsonify({
            "success":False,
            "message":"Email already exists."
        })

    cursor.execute(
        """
        INSERT INTO users
        (first_name,last_name,email,password)
        VALUES(?,?,?,?)
        """,
        (
            first_name,
            last_name,
            email,
            password
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success":True,
        "message":"Register Successful."
    })

@app.route("/login", methods=["POST"])
def login():
    request_data = request.get_json()
    email = request_data["email"].strip()
    password = request_data["password"]

    if email == "" or password == "":
        return jsonify({
            "success":False,
            "message":"Please fill in all fields."
        })
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email=? AND password=?
        """,
        (
            email,
            password
        )
    )

    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify({
            "success":True,
            "user_id":user[0],
            "first_name":user[1],
            "last_name":user[2]
        })
    return jsonify({
        "success":False,
        "message":"Invalid email or password."
    })

if __name__ == "__main__":
    app.run(debug=True)