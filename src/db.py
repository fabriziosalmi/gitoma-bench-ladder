from __future__ import annotations

import sqlite3


def get_conn() -> sqlite3.Connection:
    """Open an in-memory SQLite connection with row-dict access."""
    conn = sqlite3.connect(
        ":memory:",
        check_same_thread=False
    )
    conn.row_factory = sqlite3.Row
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id   INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """
    )


def seed(conn: sqlite3.Connection) -> None:
    conn.executemany(
        "INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)",
        [(1, "alice"), (2, "bob"), (3, "carol")],
    )
    conn.commit()


def find_user_by_name(conn: sqlite3.Connection, name: str) -> list[dict]:
    """Return all users whose name equals ``name``.

    BUG (the only one in this file): the SQL is built by f-string
    interpolation. A malicious ``name`` containing a single quote can
    break out of the literal and inject arbitrary SQL. The fix is to
    use a parameterised query — sqlite3 supports ``?`` placeholders
    natively.
    """
    cur = conn.execute("SELECT id, name FROM users WHERE name = ?", (name,))
    return [dict(row) for row in cur]