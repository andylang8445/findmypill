import search_handler as sh
import db_communicate as dbm


def add_ingredient(ingredient_dict: dict(), din_code: str, pill_id: int = -1):
    if pill_id == -1:
        alias_din_cnt, = sh.search_by_din(str(din_code))
        if alias_din_cnt > 1:
            print("Please provide pill_id as alias exists in the DB")
            return -1
        elif alias_din_cnt == 0:
            print("Given DIN does not exist\nCheck DB")
            return -2
        else:
            
    else:
        count, _ = sh.search_by_pill_id(str(pill_id), True)
        if count > 1:
            print("Given pill_id is not unique\n"
                  "There should not be conflicting pill_id in DB\n"
                  "Please check DB")
        elif count == 0:
            print("Given pill_id does not exist\n"
                  "Check given pill_id and try again")




def add_pill_spec(name: str, company: str, type_info: str, consume_info: str, din_code: str, alias_count: int = 0):
    pill_dict = dict()
    pill_dict['name'] = name
    pill_dict['company'] = company
    pill_dict['DIN'] = din_code
    pill_dict['type'] = type_info
    pill_dict['consume'] = consume_info
    counter, _ = sh.search_by_din(str(din_code), alias_count)
    if counter == 0 or counter < alias_count:
        # proceed
        pill_dict['id'] = int(dbm.data_counter('Pill_Specification')) + 1
        print(pill_dict)
        val = dbm.add_new_pill(pill_dict)
        if val == 200:
            new_cnt, _ = sh.search_by_din(din_code, alias_count)
            if new_cnt == (counter + 1):
                return "Successfully added to DB"
            else:
                return "Unknown ERROR Occurred." \
                       "\nQuery was made successfully, but was not able to check if it was made to the server"
        else:
            return "Unknown ERROR Occurred." \
                   "\nQuery was not made successfully"
    else:
        # error, pill with DIN already exists
        if alias_count > 0:
            return "More pill with same DIN are present in DB than expected"
        else:
            return "error, pill with the given DIN already exists"


print("result: ", add_pill_spec('tester', 'Andy Yun', 'Object', 'USB', '23', 9999))
