import sqlite3
from typing import Optional

# Assume conn is established elsewhere or passed in contextually

def get_conn() -> sqlite3.Connection:
    # Placeholder implementation for demonstration
    conn = sqlite3.connect("test.db")
    return conn

def init_schema(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL)"
    )

def find_user_by_name(conn: sqlite3.Connection, name: str) -> Optional[tuple]:
    """Finds a user by name using parameterized query to prevent SQL injection."""
    # FIX: Replaced f-string interpolation with parameterized query.
    cur = conn.execute(
        "SELECT id, name FROM users WHERE name = ?",
        (name),
    )
    return cur.fetchone()

def seed(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (name) VALUES (?)",
        ("alice"),
    )
    cursor.execute(
        "INSERT OR IGNORE INTO users (name) VALUES (?)",
        ("bob"),
    )
    cursor.execute(
        "INSERT OR IGNORE INTO users (name) VALUES (?)",
        ("charlie"),
    )