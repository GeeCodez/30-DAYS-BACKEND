import sqlite3

DB_NAME = "guessing_game.db"

def get_connection():
    """Return a sqlite3 connection."""
    with sqlite3.connect(DB_NAME) as conn:
        return conn


def initialize_database():
    """Run only once at startup to create required tables."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT,
            difficulty TEXT,
            attempts_used INTEGER,
            max_attempts INTEGER,
            secret_number INTEGER,
            status TEXT,
            time TEXT
        )
    """)

    conn.commit()
    conn.close()
