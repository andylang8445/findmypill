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
    :return string data of the pill info:
    """
    val: str = str()
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
        for (name, element, id_code, din_code, company_name, dose_form, how_to_consume) in query_return:
            li = element.split(',')

    # search cache
    # search DB
    # Update cache based on the data
    # Return the value


def get_element(el_code: int):
    """
    :param el_code:  element code
    :return: name of the corresponding element
    """
    # search cache
    # search DB
    # Update cache based on the data
    # Return the name
