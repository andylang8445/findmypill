import sys

import db_communicate as dbm
import config as c


def search_by_din(din_code: str, alias_allowed: int):
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
    if alias_allowed > 0:
        alias_cnt = alias_allowed
    if data_cnt > alias_cnt:
        print("==========================================================================")
        print("WARNING: Conflict found in DB, DIN should be an UNIQUE value of each PILL")
        print("==========================================================================")
        sys.exit(1)
    return data_cnt, result_val
