import sqlite3

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    return conn


def find_user_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    return cursor.fetchall()


def init_schema(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")


def seed(conn):
    conn.execute("INSERT INTO users (name) VALUES ('alice')")