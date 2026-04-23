import sqlite3

def find_user_by_name(conn, name):
    cursor = conn.cursor()
    query = """
    SELECT * FROM users
    WHERE name = ?
    """
    cursor.execute(query, (name,))
    return cursor.fetchall()


def get_conn():
    return sqlite3.connect(':memory:')

# init_schema and seed functions remain unchanged as they don't affect the injection vector