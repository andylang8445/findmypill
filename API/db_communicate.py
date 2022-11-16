# Module Imports
import mariadb
import sys


def connection_tester():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="localhost",
            port=3306,
            database="pill"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    print("Connection to DB Successful")
    cur = conn.cursor()
