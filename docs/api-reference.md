# API Reference

This section provides documentation for the APIs available in the gitoma-bench-ladder project.

## Modules

### src.db

The `src/db.py` module provides database-related functionality. It includes:
- Database connection setup
- Query execution
- Result handling

## Usage Examples

### Connecting to the Database

```python
from src.db import connect_to_db

connection = connect_to_db()
# Use the connection to perform database operations
```