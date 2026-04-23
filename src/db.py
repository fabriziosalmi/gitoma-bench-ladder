import psycopg2
from psycopg2 import sql

def find_user_by_name(conn, name):
    query = sql.SQL("SELECT * FROM users WHERE name = {};").format(
        sql.Literal(name)
    )
    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()