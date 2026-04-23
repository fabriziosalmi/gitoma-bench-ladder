import psycopg2
from psycopg2 import sql


def find_user_by_name(conn, name):
    """
    Find a user by their name in the database.

    Args:
        conn: A psycopg2 connection object to the database.
        name (str): The name of the user to find.

    Returns:
        list: A list of database rows representing users with the given name.

    Raises:
        psycopg2.Error: If a database error occurs during query execution.
    """
    query = sql.SQL("SELECT * FROM users WHERE name = {}; ").format(
        sql.Literal(name)
    )
    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()