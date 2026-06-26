from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import request
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/")
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

if __name__ == "__main__":
    app.run(debug=True)