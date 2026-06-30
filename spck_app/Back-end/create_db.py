import sqlite3

conn = sqlite3.connect("games.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    password TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS games(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT,
    genre TEXT,
    hours_played INTEGER,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database created.")