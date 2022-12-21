import sys

import db_communicate as dbm
import config as c


def search_by_din(din_code: str):
    result = dbm.select_operator(c.table_info['pill-name-type'], ['*'], [f'DIN = {din_code}'])
    result_val = list()
    data_cnt: int = 0
    for (id_code, name, dose_form, company_name, how_to_consume, din_code) in result:
        data_cnt += 1
        sub_dict = dict()
        sub_dict['pill_id'] = id_code
        sub_dict['name'] = name
        sub_dict['din_code'] = din_code
        sub_dict['company_name'] = company_name
        sub_dict['dose_form'] = dose_form
        sub_dict['how_to_consume'] = how_to_consume
        result_val.append(sub_dict)
    alias_cnt = 1
    if data_cnt > alias_cnt:
        # check if there is an 'IDENTICAL PILL' in DB
        print("==========================================================================")
        print("WARNING: Conflict found in DB, DIN should be an UNIQUE value of each PILL")
        print("==========================================================================")
        sys.exit(1)
    return data_cnt, result_val


def search_by_pill_id(pill_id: str, expected_to_exist: bool = False):
    result = dbm.select_operator(c.table_info['pill-name-type'], ['*'], [f'id = {pill_id}'])
    result_val = list()
    data_cnt: int = 0
    for (id_code, name, dose_form, company_name, how_to_consume, din_code) in result:
        data_cnt += 1
        sub_dict = dict()
        sub_dict['pill_id'] = id_code
        sub_dict['name'] = name
        sub_dict['din_code'] = din_code
        sub_dict['company_name'] = company_name
        sub_dict['dose_form'] = dose_form
        sub_dict['how_to_consume'] = how_to_consume
        result_val.append(sub_dict)
    if (not expected_to_exist) and data_cnt > 0:
        print("==========================================================================")
        print("Error: Conflict found in DB, DIN should be an UNIQUE value of each PILL")
        print("==========================================================================")
        sys.exit(1)
    return data_cnt, result_val


def search_ingredient_by_name(ingredient_name: str):
    val = dbm.select_operator(c.table_info['ingredient'], ['*'], [f'name = "{ingredient_name}"'])
    counter = 0
    return_val = []
    for (id_code, name) in val:
        counter += 1
        return_val.append({str(name): str(id_code)})
    if counter > 1:
        print("Warning: There are ingredients with same name")
    if counter <= 0:
        return False, []
    else:
        return True, return_val
