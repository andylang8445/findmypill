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
    ingredient_cur.execute("SELECT Code FROM %s;" % str(c.table['ingredient']))
    return_val = []
    element_li = []
    for (i,) in ingredient_cur:
        element_li.append(int(i))
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM %s;" % str(c.table['pill'])
    )
    for (name, element, id_code, din_code, company_name, dose_form, how_to_consume) in cur:
        sub_dict = dict()
        print(f"Name of the pill: {name}, ", end="[")
        li = element.split(',')
        sub_li = list()
        for i in li:
            ingredient, amount = i.split(':')
            if int(ingredient) in element_li:
                ingredient_cur = conn.cursor()
                ingredient_cur.execute(
                    "SELECT Ingredient FROM %s WHERE Code = %s;" % (str(c.table['ingredient']), ingredient)
                )
                tmp_ingredient = list(ingredient_cur)[0][0]
                sub_li.append({tmp_ingredient: str(amount) + "mg"})
                print("[ingredient: ", tmp_ingredient, ", amount = ", amount, end="mg], ")
            elif int(ingredient) != -1:
                print(f"[Unknown ingredient! Please check DB! (Unknown ingredient: {ingredient})], ", end=", ")
        sub_dict['ingredient'] = sub_li
        if len(str(id_code)) == 0:
            id_code = 'N/A'
        if len(din_code) == 0:
            din_code = 'N/A'
        if len(company_name) == 0:
            company_name = 'N/A'
        if len(dose_form) == 0:
            dose_form = 'N/A'
        if len(how_to_consume) == 0:
            how_to_consume = 'N/A'
        sub_dict['name'] = name
        sub_dict['id_code'] = id_code
        sub_dict['din_code'] = din_code
        sub_dict['company_name'] = company_name
        sub_dict['dose_form'] = dose_form
        sub_dict['how_to_consume'] = how_to_consume
        print(
            f"], id: {id_code}, DIN code: {din_code}, Produced by: {company_name}, Form: {dose_form}, Route of Administration: {how_to_consume}")
        return_val.append(sub_dict)
    return return_val


def execute_new(query_str: str, data: tuple):
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
    cur = conn.cursor()
    cur.execute(
        query_str, data
    )
    return cur
