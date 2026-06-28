from flask import Flask, jsonify, request
from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Game Collection Manager"

@app.route("/games", methods=["GET"])
def get_games():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route("/games", methods=["POST"])
def add_game():
    request_data = request.get_json()
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute(
    """
    INSERT INTO games
    (name, genre, hours_played, status)
    VALUES(?, ?, ?, ?)
    """,
    (
        request_data["user_id"],
        request_data["name"],
        request_data["genre"],
        request_data["hours_played"],
        request_data["status"]
    )
    )
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

    username = request_data["username"].strip()
    password = request_data["password"].strip()

    if username == "" or password == "":
        return jsonify({
            "success": False,
            "message": "Please fill in all fields."
        })

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    if user:
        conn.close()
        return jsonify({
            "success": False,
            "message": "Username already exists."
        })

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username,password)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Register successful."
    })

@app.route("/login", methods=["POST"])
def login():

    request_data = request.get_json()

    username = request_data["username"].strip()
    password = request_data["password"].strip()

    if username == "" or password == "":
        return jsonify({
            "success": False,
            "message": "Please fill in all fields."
        })

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({
            "success": True,
            "user_id": user[0],
            "username": user[1]
        })

    return jsonify({
        "success": False,
        "message": "Wrong username or password."
    })

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

if __name__ == "__main__":
    app.run(debug=True)