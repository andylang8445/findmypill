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
    ingredient_cur = conn.cursor()
    ingredient_cur.execute(
        f"SELECT Code FROM {c.table['ingredient']}"
    )
    element_li = []
    for (i,) in ingredient_cur:
        element_li.append(int(i))
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM {c.table['pill']}"
    )
    for (name, element, id_code) in cur:
        print(f"Name of the pill: {name}, ", end="[")
        li = element.split(',')
        for i in li:
            ingredient, amount = i.split(':')
            if int(ingredient) in element_li:
                ingredient_cur = conn.cursor()
                ingredient_cur.execute(
                    f"SELECT Ingredient FROM {c.table['ingredient']} WHERE Code = {ingredient}"
                )
                print("[ingredient: ", list(ingredient_cur)[0][0], ", amount = ", amount, end="mg], ")
            elif int(ingredient) != -1:
                print(f"[Unknown ingredient! Please check DB! (Unknown ingredient: {ingredient})], ", end=", ")
        print("], id: ", id_code)
