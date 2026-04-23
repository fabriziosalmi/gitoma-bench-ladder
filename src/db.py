import sqlite3

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    return conn


def init_schema(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    ''')


def seed(conn):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('alice',))


def find_user_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM users WHERE name = ?', (name,))
    return [dict(row) for row in cursor]