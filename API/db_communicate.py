# Module Imports
import mariadb
import sys
import config as c


def viewer_obj_creator():
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
    return conn


def remover_obj_creator():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=c.remover['id'],
            password=c.remover['pw'],
            host=c.DB['host'],
            port=c.DB['port'],
            database=c.DB['db_name']

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn


def adder_obj_creator():
    # Connect to MariaDB Platform
    try:
        add_conn = mariadb.connect(
            user=c.adder['id'],
            password=c.adder['pw'],
            host=c.DB['host'],
            port=c.DB['port'],
            database=c.DB['db_name']

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return add_conn


def connection_tester():
    # Connect to MariaDB Platform
    conn = viewer_obj_creator()

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
            "SELECT %s,%s FROM %s WHERE id=%s;" % (
            'Material_Info', 'amount', c.table_info['pill-ingredient'], str(id_code))
        )
        print(f"Name of the pill: {name}, ", end="Ingredients: [")
        mat_li = list()
        for (material_id, amount) in pill_ingredient_cur:
            tmp = {'ingredient_id': int(material_id), 'ingredient_name': str(element_dict[int(material_id)]),
                   'ingredient_amount': int(str(amount).split(' ')[0]), 'ingredient_unit': str(amount).split(' ')[1]}
            mat_li.append(tmp)
            print("[ingredient id: %d, name: %s, amount: %d, unit: %s]" % (
            tmp['ingredient_id'], tmp['ingredient_name'], tmp['ingredient_amount'], tmp['ingredient_unit']), end=', ')
        print(
            f"], Pill id: {id_code}, Dose Form: {dose_form}, Produced By: {company_name}, Route of Administration: {how_to_consume}, DIN code: {din_code}")
        sub_dict['pill_id'] = id_code
        sub_dict['name'] = name
        ingredient_dict_jsonify = dict()
        ingredient_dict_jsonify['total_number'] = len(mat_li)
        for i in range(len(mat_li)):
            ingredient_dict_jsonify[int(i)] = mat_li[i]
        sub_dict['ingredient'] = ingredient_dict_jsonify
        sub_dict['din_code'] = din_code
        sub_dict['company_name'] = company_name
        sub_dict['dose_form'] = dose_form
        sub_dict['how_to_consume'] = how_to_consume
        return_val.append(sub_dict)
    conn.commit()
    conn.close()
    return return_val


def compareList(l1: list, l2: list):
    l1c = list(l1.copy())
    l2c = list(l2.copy())
    l1c.sort()
    l2c.sort()
    if l1c == l2c:
        return True
    else:
        return False


def data_counter(source: str):
    if source in list(c.table_info.values()):
        conn = viewer_obj_creator()
        counter_cur = conn.cursor()
        counter_cur.execute("SELECT COUNT(*) FROM %s;" % source)
        for i in counter_cur:
            # print(i[0])
            return i[0]
    else:
        print("Wrong SELECT FROM argument (table name mismatch)")
        return -1


def add_new_pill(info_dict: dict):
    key_chain = set(info_dict.keys())
    db_alias = list(c.columns_info['Pill_Specification'].keys())
    if not compareList(key_chain, db_alias):
        print("Given Data is not containing the correct data")
        return -1
    query_string = 'INSERT INTO ' + c.table_info['pill-name-type'] + ' ('
    for i in range(len(db_alias)):
        query_string += str(db_alias[i])
        if i < (len(db_alias) - 1):
            query_string += ','
    query_string += ') VALUES ('
    for i in range(len(db_alias)):
        query_string += '"' + str(info_dict[str(db_alias[i])]) + '"'
        if i < (len(db_alias) - 1):
            query_string += ','
        else:
            query_string += ');'
    print(query_string)
    conn = adder_obj_creator()
    new_pill_cur = conn.cursor()
    try:
        new_pill_cur.execute(query_string)
    except mariadb.Error as e:
        print(f'Error: {e}')
    conn.commit()
    conn.close()
    return 200


def add_new_pill_ingredient_relationship(info_dict: dict()):
    key_chain = set(info_dict.keys())
    db_alias = list(c.columns_info['Pill_Info'].keys())
    if not compareList(key_chain, db_alias):
        print("Given Data is not containing the correct data")
        return -1
    query_string = 'INSERT INTO ' + c.table_info['pill-ingredient'] + ' ('
    for i in range(len(db_alias)):
        query_string += str(db_alias[i])
        if i < (len(db_alias) - 1):
            query_string += ','
    query_string += ') VALUES ('
    for i in range(len(db_alias)):
        query_string += '"' + str(info_dict[str(db_alias[i])]) + '"'
        if i < (len(db_alias) - 1):
            query_string += ','
        else:
            query_string += ');'
    print(query_string)
    conn = adder_obj_creator()
    new_pill_cur = conn.cursor()
    try:
        new_pill_cur.execute(query_string)
    except mariadb.Error as e:
        print(f'Error: {e}')
    conn.commit()
    conn.close()
    return 200


def add_new_ingredient(info_dict: dict):
    key_chain = set(info_dict.keys())
    db_alias = list(c.columns_info['Material_Info'].keys())
    if not compareList(key_chain, db_alias):
        print("Given Data is not containing the correct data")
        return -1
    query_string = 'INSERT INTO ' + c.table_info['ingredient'] + ' ('
    for i in range(len(db_alias)):
        query_string += str(db_alias[i])
        if i < (len(db_alias) - 1):
            query_string += ','
    query_string += ') VALUES ('
    for i in range(len(db_alias)):
        query_string += '"' + str(info_dict[str(db_alias[i])]) + '"'
        if i < (len(db_alias) - 1):
            query_string += ','
        else:
            query_string += ');'
    print(query_string)
    conn = adder_obj_creator()
    new_pill_cur = conn.cursor()
    try:
        new_pill_cur.execute(query_string)
    except mariadb.Error as e:
        print(f'Error: {e}')
    conn.commit()
    conn.close()
    return 200


def remove_operator(source: str, condition: list = []):
    print(source, condition)
    query_string = "DELETE FROM "
    if source in list(c.table_info.values()):
        query_string += source
    else:
        print("Wrong SELECT FROM argument (table name mismatch)")
        return [-2]
    if len(condition) == 0:
        print("Missing Condition in DELETE operation (Cannot be Empty)")
        return [-1]
    else:
        query_string += ' WHERE '
        for i in range(len(condition)):
            query_string += condition[i]
            if i < (len(condition) - 1):
                query_string += ' and '
        query_string += ';'
    print(query_string)
    conn = remover_obj_creator()
    remove_cur = conn.cursor()
    remove_cur.execute(query_string)
    conn.commit()
    conn.close()
    return [200]


def select_operator(source: str, what: list = ['*'], condition: list = []):
    query_string = "SELECT "
    if len(what) == 1:
        query_string += what[0].strip(' ').strip('\n').strip('\t')
    elif len(what) == 0:
        print("Wrong SELECT argument (No target to select from)")
        return [-1]
    else:
        for i in range(len(what)):
            tmp = str(what[i]).strip(' ', '\n', '\t')
            query_string += tmp
            if i < (len(what) - 1):
                query_string += ','
    query_string += ' FROM '
    if source in list(c.table_info.values()):
        query_string += source
    else:
        print("Wrong SELECT FROM argument (table name mismatch)")
        return [-2]
    if len(condition) == 0:
        query_string += ';'
    else:
        query_string += ' WHERE '
        for i in range(len(condition)):
            query_string += condition[i]
            if i < (len(condition) - 1):
                query_string += ' and '
        query_string += ';'
    conn = viewer_obj_creator()
    select_cur = conn.cursor()
    print("The following is the query string:\n\t")
    print(query_string)
    select_cur.execute(query_string)
    return select_cur


def execute_new(query_str: str, data: tuple):
    conn = viewer_obj_creator()
    cur = conn.cursor()
    cur.execute(
        query_str, data
    )
    conn.commit()
    conn.close()
    return cur
