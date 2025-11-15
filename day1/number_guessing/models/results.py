from datetime import datetime
from db.connection import get_connection

def save_result(player, difficulty, attempts_used, max_attempts, secret_number, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO results (player, difficulty, attempts_used, max_attempts, secret_number, status, time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        player, difficulty, attempts_used, max_attempts, secret_number, status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()

def get_history(player):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results WHERE player = ?", (player,))
    rows = cursor.fetchall()
    conn.close()
    return rows
