# Module Imports
import mariadb
import sys
import config as c


def connection_tester():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=c.viewer['id'],
            password=c.viewer['pw'],
            host=c.DB['host'],
            port=c.DB['port'],
            database=c.DB['db_name']

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    print("Connection to DB Successful")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM test"
    )
    for (name, element, id_code) in cur:
        print(f"Name of the pill: {name}, ", end="[")
        li = element.split(',')
        for i in li:
            ingredient, amount = i.split(':')
            ingredient_cur = conn.cursor()
            ingredient_cur.execute(
                f"SELECT Ingredient FROM element WHERE Code = {ingredient}"
            )
            if ingredient != '-1':
                print("[ingredient: ", list(ingredient_cur)[0][0], ", amount = ", amount, end="mg], ")
            else:
                print("END of ingredients]")
        print("id: ", id_code)


