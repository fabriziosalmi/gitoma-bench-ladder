import os
from .db import connect_to_database

def main():
    connection = connect_to_database()
    print("Connected to database")

if __name__ == "__main__":
    main()