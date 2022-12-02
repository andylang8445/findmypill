import config as c
from db_communicate import execute_new as query_server
import mariadb

pill_cache_key = list()
pill_cache = list()
pill_access_counter = list()
pill_cache_timestamp = list()
el_cache_key = list()
el_cache = list()


def get_pill(din_code: str):
    """
    :param din_code: medication code
    :return dict data of the pill info:
    """
    val: dict = dict()
    if din_code in pill_cache_key:
        pill_idx: int = pill_cache_key.index(din_code)
        pill_access_counter[pill_idx] += 1
        val = pill_cache[pill_idx]
    else:
        if len(pill_cache) > c.max_pill_cache:
            val_to_be_deleted = pill_cache_timestamp.index(min(pill_cache_timestamp))
            pill_cache_key.pop(val_to_be_deleted)
            pill_cache.pop(val_to_be_deleted)
            pill_access_counter.pop(val_to_be_deleted)
            pill_cache_timestamp.pop(val_to_be_deleted)
        # Query the server
        query_string = "SELECT * FROM %s WHERE DIN = %s;"
        query_data = (str(c.table['pill']), din_code)
        query_return = query_server(query_string, query_data)
        return_li = list()
        for (name, element, id_code, din_code, company_name, dose_form, how_to_consume) in query_return:
            li = element.split(',')
            sub_li: list = list()
            sub_dict = dict()
            for el_each in li:
                ingredient_str: str = ''
                amount: str = ''
                ingredient_str, amount = el_each.split(':')
                el_name_str = get_element(int(ingredient_str))
                sub_li.append({el_name_str: str(amount) + "mg"})
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
            return_li.append(sub_dict)
        return return_li[0]

    # search cache
    # search DB
    # Update cache based on the data
    # Return the value


def get_element(el_code: int) -> str:
    """
    :param el_code:  element code
    :return: name of the corresponding element
    """
    query_string = "SELECT Ingredient FROM %s WHERE Code = %s;"
    query_data = (str(c.table['ingredient']), el_code)
    query_return = query_server(query_string, query_data)
    tmp_ingredient = list(query_return)[0][0]
    return str(tmp_ingredient)
    # search cache
    # search DB
    # Update cache based on the data
    # Return the name
