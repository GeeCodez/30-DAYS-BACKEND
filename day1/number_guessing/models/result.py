from datetime import datetime
from db.connection import get_connection

def save_result(player, difficulty, attempts_used, max_attempts, secret_number, status):
    """Insert a game result into the database."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO results (player, difficulty, attempts_used, max_attempts, secret_number, status, time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        player,
        difficulty,
        attempts_used,
        max_attempts,
        secret_number,
        status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_history(player):
    """Retrieve all game history for a specific player."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM results WHERE player = ?", (player,))
    rows = cursor.fetchall()

    conn.close()
    return rows
