import pytest

from src.db import find_user_by_name, get_conn, init_schema, seed


@pytest.fixture
def db():
    conn = get_conn()
    init_schema(conn)
    seed(conn)
    return conn


def test_find_known_user(db):
    rows = find_user_by_name(db, "alice")
    assert len(rows) == 1
    assert rows[0]["name"] == "alice"


def test_find_unknown_user_returns_empty(db):
    assert find_user_by_name(db, "dave") == []


def test_no_sql_injection(db):
    """A malicious name designed to bypass the WHERE clause must NOT
    return all rows. Pre-fix this leaks every user; post-fix the input
    is treated as a literal name (which doesn't match any real user) and
    the result is empty."""
    payload = "' OR '1'='1"
    rows = find_user_by_name(db, payload)
    assert rows == [], (
        f"SQL injection succeeded: leaked {len(rows)} row(s) — "
        "the function builds queries by string concatenation. "
        "Fix: use a parameterised query (? placeholder)."
    )


def test_no_sql_injection_via_comment(db):
    """A second injection vector: SQL line comment to truncate the query.
    Mirrors a real-world payload pattern."""
    payload = "alice'; --"
    rows = find_user_by_name(db, payload)
    assert rows == [], (
        f"SQL comment injection succeeded: leaked {len(rows)} row(s)."
    )
