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
    conn.close()
    return jsonify({
        "total":total,
        "playing":playing,
        "completed":completed
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

if __name__ == "__main__":
    app.run(debug=True)