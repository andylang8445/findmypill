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
    ingredient_cur.execute("SELECT * FROM %s;" % (c.table_info['ingredient']))
    return_val = []
    element_dict = dict()
    for (i, name) in ingredient_cur:
        element_dict[int(i)] = str(name)
    pill_name_type_cur = conn.cursor()
    pill_name_type_cur.execute(
        "SELECT * FROM %s ORDER BY id;" % str(c.table_info['pill-name-type'])
    )
    for (id_code, name, dose_form, company_name, how_to_consume, din_code) in pill_name_type_cur:
        print("AA")
        sub_dict = dict()
        pill_ingredient_cur = conn.cursor()
        pill_ingredient_cur.execute(
            "SELECT %s,%s FROM %s WHERE id=%s;" % ('Material_Info', 'amount', c.table_info['pill-ingredient'], str(id_code))
        )
        print(f"Name of the pill: {name}, ", end="Ingredients: [")
        mat_li = list()
        for (material_id, amount) in pill_ingredient_cur:
            tmp = [int(material_id), str(element_dict[int(material_id)]), int(str(amount).split(' ')[0]), str(amount).split(' ')[1]]
            mat_li.append(tmp)
            print("[ingredient id: %d, name: %s, amount: %d, unit: %s]" % (tmp[0], tmp[1], tmp[2], tmp[3]), end=', ')
        print(f"], Pill id: {id_code}, Dose Form: {dose_form}, Produced By: {company_name}, Route of Administration: {how_to_consume}, DIN code: {din_code}")
        sub_dict['pill_id'] = id_code
        sub_dict['name'] = name
        sub_dict['ingredient'] = mat_li
        sub_dict['din_code'] = din_code
        sub_dict['company_name'] = company_name
        sub_dict['dose_form'] = dose_form
        sub_dict['how_to_consume'] = how_to_consume
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
