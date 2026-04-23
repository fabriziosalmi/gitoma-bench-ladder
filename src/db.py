def find_user_by_name(conn: sqlite3.Connection, name: str) -> list[dict]:
    """Return all users whose name equals ``name``.

    BUG (the only one in this file): the SQL is built by f-string
    interpolation. A malicious ``name`` containing a single quote can
    break out of the literal and inject arbitrary SQL. The fix is to
    use a parameterised query -- sqlite3 supports ``?`` placeholders
    natively.
    """
    cur = conn.execute("SELECT id, name FROM users WHERE name = ?", (name,))
    return [dict(row) for row in cur]