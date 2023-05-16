import config as c
from tinydb import *
import search_handler as sh
import ldbm_config as lc


def erase_all_data_from_table():
    db = TinyDB(lc.db_file)
    table = db.table(lc.table_name)
    table.truncate()
    return 200


def increment_item(ing_li: list, pill_li: list):
    ing_inc_queue = list()
    if len(pill_li) > 0:
        for i in pill_li:
            tmp_ing_li = sh.get_ingredient_by_id(str(i))
            ing_inc_queue += tmp_ing_li
    ing_inc_queue += ing_li
    if len(ing_inc_queue) > 0:
        db = TinyDB(lc.db_file)
        table = db.table(lc.table_name)
        for i in ing_inc_queue:
            # perform increment in local db
            pass
        return 200
    else:
        return 500


def tester():
    db = TinyDB(lc.db_file)
    table = db.table(lc.table_name)
    print(table.all())
    table.insert({'name': 'Andy', 'code': 1})
    print(table.all())
    table.truncate()
    print(table.all())


tester()
