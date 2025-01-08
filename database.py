import sqlite3

DATABASE = "weather.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_history(city):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (city) VALUES (?)", (city,))
    conn.commit()
    conn.close()


def get_history(limit=5):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT city FROM history ORDER BY id DESC LIMIT ?", (limit,))
    history = [row[0] for row in cursor.fetchall()]
    conn.close()
    return history
