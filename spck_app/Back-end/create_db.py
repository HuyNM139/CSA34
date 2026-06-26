import sqlite3
conn = sqlite3.connect("games.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    genre TEXT,
    hours_played INT,
    status TEXT
)
""")
conn.commit()
conn.close()
print("Database created")