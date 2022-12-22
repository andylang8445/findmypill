import search_handler as sh
import db_communicate as dbm
import config as c


def delete_pill(din_code, id_code=-1):
    din_alias_count, din_alias_list = sh.search_by_din(str(din_code))
    remove_target_id = -1
    if din_alias_count <= 0:
        return "Given DIN does not exist in the record", 404
    elif din_alias_count == 1:
        if (str(din_alias_list[0]['pill_id']) == str(id_code)) or (id_code == -1):
            # remove the given str(din_alias_list[0]['pill_id']) pill
            remove_target_id = str(din_alias_list[0]['pill_id'])
            pass
        else:
            return "Given ID code does not match our DB", 404
    else:
        remove_target = -1
        for i in din_alias_list:
            if str(i['pill_id']) == str(id_code):
                remove_target = int(str(id_code))
                remove_target_id = str(id_code)
                break
        if remove_target == -1:
            return "Given DIN code has multiple pills, and given id_code is not associated to one of them", 404
    val = dbm.remove_operator(c.table_info['pill-ingredient'], [f'id = {remove_target_id}'])
    if val[0] != 200:
        return f"Pill with ID {remove_target_id} failed to be removed from {c.table_info['pill-ingredient']} table", 503
    val = dbm.remove_operator(c.table_info['pill-name-type'], [f'id = {remove_target_id}'])
    if val[0] != 200:
        return f"Pill with ID {remove_target_id} failed to be removed from {c.table_info['pill-name-type']} table", 503
    return f"Pill with ID {remove_target_id} removed successfully", 200


msg, code = delete_pill(50030441)

print(msg, code)
