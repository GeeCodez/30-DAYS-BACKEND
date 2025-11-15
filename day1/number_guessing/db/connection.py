import sqlite3

DB_NAME = "guessing_game.db"

def get_connection():
    """Return a sqlite3 connection."""
    return sqlite3.connect(DB_NAME)

def initialize_database():
    """Create results table if it doesn't exist."""
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
