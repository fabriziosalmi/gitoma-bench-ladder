import sqlite3

def get_conn():
    return sqlite3.connect(':memory:')

def init_schema(conn):
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')

def seed(conn):
    conn.execute('INSERT INTO users (name) VALUES (?)', ('alice',))

def find_user_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    return [dict(row) for row in cursor.fetchall()]