import search_handler as sh
import db_communicate as dbm


def add_ingredient(ingredient_dict: dict(), din_code: str, pill_id: int = -1):
    if pill_id == -1:
        alias_din_cnt, result_val = sh.search_by_din(str(din_code))
        if alias_din_cnt == 0:
            print("Given DIN does not exist\nCheck DB")
            return -1
        elif alias_din_cnt > 1:
            print("Please specify pill_id as there are multiple pills with same DIN")
            return -4
        else:
            pill_id = int(result_val[0]['pill_id'])
    else:
        count, _ = sh.search_by_pill_id(str(pill_id), True)
        if count > 1:
            print("Given pill_id is not unique\n"
                  "There should not be conflicting pill_id in DB\n"
                  "Please check DB")
            return -2
        elif count == 0:
            print("Given pill_id does not exist\n"
                  "Check given pill_id and try again")
            return -3
    included_ingredient_li = list(ingredient_dict.keys())
    pill_info_add_queue = list()
    material_info_add_queue = list()
    for each_ing in included_ingredient_li:
        ing = str(each_ing).upper()
        flag, resulting_li = sh.search_ingredient_by_name(str(ing))
        if flag:
            pill_info_add_queue.append({'id': pill_id, 'Material_Info': resulting_li[0][str(ing)],
                                        'amount': f'{ingredient_dict[str(each_ing)][0]} {ingredient_dict[str(each_ing)][1]}'})
        else:
            tmp_ingredient_code = int(len(material_info_add_queue) + dbm.data_counter('Material_Info') + 1)
            pill_info_add_queue.append({'id': pill_id, 'Material_Info': tmp_ingredient_code,
                                        'amount': f'{ingredient_dict[str(each_ing)][0]} {ingredient_dict[str(each_ing)][1]}'})
            material_info_add_queue.append({'id': tmp_ingredient_code, 'name': str(ing)})
    for line in material_info_add_queue:
        val = dbm.add_new_ingredient(line)
        if val == 200:
            print(f'\tIngredient ID {line["id"]} have ben added to DB')
        else:
            print(f"ERROR Occurred while adding Ingredient ID {line['id']} to DB")
    for line in pill_info_add_queue:
        val = dbm.add_new_pill_ingredient_relationship(line)
        if val == 200:
            print(f'\tRelationship between PillID {line["id"]} and IngredientID {line["Material_Info"]} have ben added '
                  f'to DB')
        else:
            print(f"\tERROR Occurred while adding relationship between PillID {line['id']} and IngredientID {line['Material_Info']} to DB")
    print(f"\t{len(pill_info_add_queue)} new Pill-Ingredient relationships and \n\t"
          f"{len(material_info_add_queue)} new Ingredients have been added to FMP DB")
    return 200






def add_pill_spec(name: str, company: str, type_info: str, consume_info: str, din_code: str):
    pill_dict = dict()
    pill_dict['name'] = name
    pill_dict['company'] = company
    pill_dict['DIN'] = din_code
    pill_dict['type'] = type_info
    pill_dict['consume'] = consume_info
    counter, conflict_check_li = sh.search_by_din(str(din_code))
    if counter > 0:
        # check if identical stuff are present
        for item in conflict_check_li:
            flag = True
            flag &= (item['name'] == name)
            flag &= (item['company_name'] == company)
            flag &= (item['din_code'] == din_code)
            flag &= (item['dose_form'] == type_info)
            flag &= (item['how_to_consume'] == consume_info)
            if flag:
                return "Perfect Duplicat Found in DB\nPlease check DB, Nothing added to DB", -9

    # proceed
    pill_dict['id'] = int(dbm.data_counter('Pill_Specification')) + 1
    print(pill_dict)
    val = dbm.add_new_pill(pill_dict)
    if val == 200:
        new_cnt, _ = sh.search_by_din(din_code)
        if new_cnt == (counter + 1):
            return "Successfully added to DB", pill_dict['id']
        else:
            return "Unknown ERROR Occurred." \
                   "\nQuery was made successfully, but was not able to check if it was made to the server", -1
    else:
        return "Unknown ERROR Occurred." \
               "\nQuery was not made successfully", -1

def add_new_pill(pill_dict: dict):
    return_val, new_id = add_pill_spec(pill_dict['name'], pill_dict['company'], pill_dict['type_info'], pill_dict['consume_info'], pill_dict['din_code'])
    print("\tresult from add_pill_spec:\n", return_val)
    print("====================")
    if new_id > 0:
        return_val = add_ingredient(pill_dict['ingredient'], pill_dict['din_code'], new_id)
    else:
        print("ERROR Occurred while running add_pill_spec function. Check DATA")
        return -1
    if return_val == 200:
        print("Added all the information into DB")
        return 200
    else:
        print("ERROR Occurred while running add_ingredient, but add_pill_spec executed successfully")
        return -1


new_pill_dict = {'name': 'tester', 'company': 'Andy Yun', 'type_info': 'tester', 'consume_info': 'data_check', 'din_code': '500304412', 'ingredient': {
    'ACETAMINOPHEN': [500, 'kg'],
    'DEXTROMETHORPHAN HYDROBROMIDE': [1, 'T'],
    'New_MateriaL': [99, 'GB']
}}
# print("result: ", add_pill_spec('tester', 'Andy Yun', 'Object', 'USB', '23', 9999))
print("result: ", add_new_pill(new_pill_dict))
