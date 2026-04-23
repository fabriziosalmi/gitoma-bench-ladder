import pytest

from src.db import find_user_by_name, get_conn, init_schema, seed


def test_no_sql_injection_via_comment(db):
    """A second injection vector: SQL line comment to truncate the query.
    Mirrors a real-world payload pattern."""
    payload = "alice'; --"
    rows = find_user_by_name(db, payload)
    assert rows == [], (
        f"SQL comment injection succeeded: leaked {len(rows)} row(s)."
    )