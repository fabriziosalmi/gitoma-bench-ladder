import sqlite3

"""
Database connection and utility functions for SQLite.

Public symbols:
- get_conn: Creates a new in-memory SQLite connection.
- init_schema: Initializes the database schema.
- seed: Populates the database with sample data.
- find_user_by_name: Finds a user by name from the database.
"""

def get_conn():
    """
    Creates a new in-memory SQLite connection.

    Returns:
        sqlite3.Connection: A new database connection.
    """
    return sqlite3.connect(':memory:')

"""
Initializes the database schema by creating the users table if it doesn't exist.

Args:
    conn (sqlite3.Connection): An active database connection.
"""
def init_schema(conn):
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')

"""
Populates the database with sample data by inserting a user named 'alice'.

Args:
    conn (sqlite3.Connection): An active database connection.
"""
def seed(conn):
    conn.execute('INSERT INTO users (name) VALUES (?)', ('alice',))

"""
Finds a user by name from the database.

Args:
    conn (sqlite3.Connection): An active database connection.
    name (str): The name of the user to find.

Returns:
    list: A list of dictionaries representing the found users.
"""
def find_user_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    return [dict(row) for row in cursor.fetchall()]