import sqlite3

# ... (rest of file content)

def find_user_by_name(conn, name):
    # FIX: Use parameter binding to prevent SQL injection
    cur = conn.execute(
        "SELECT id, name FROM users WHERE name = ?",
        (name),
    )
    return cur.fetchone()

# ... (rest of file content)