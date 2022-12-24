from flask import Flask, request, jsonify
import db_communicate as dbm
import json
import register as mkp
import remover as rmp

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/tester', methods=['POST'])
def tester():
    print("=========")
    json_obj = request.get_json()
    pill_info_pict = dict()
    pill_info_pict['name'] = json_obj['name']
    pill_info_pict['company'] = json_obj['company']
    pill_info_pict['type_info'] = json_obj['type_info']
    pill_info_pict['consume_info'] = json_obj['consume_info']
    pill_info_pict['din_code'] = json_obj['din_code']
    pill_info_pict['ingredient'] = json_obj['ingredient']
    print(pill_info_pict)
    return f"complete, {str(json_obj)}, {str(type(json_obj))}"


@app.route('/add_new_pill', methods=['POST'])
def add_new_pill():
    json_obj = request.get_json()
    pill_info_pict = dict()
    '''
    {'name': 'tester', 'company': 'Andy Yun', 'type_info': 'USB', 'consume_info': 'data_check', 'din_code': '50030441', 'ingredient': {
    'ACETAMINOPHEN': [500, 'kg'],
    'DEXTROMETHORPHAN HYDROBROMIDE': [1, 'T'],
    'New_MateriaL': [99, 'GB']
}}
    '''
    pill_info_pict['name'] = json_obj['name']
    pill_info_pict['company'] = json_obj['company']
    pill_info_pict['type_info'] = json_obj['type_info']
    pill_info_pict['consume_info'] = json_obj['consume_info']
    pill_info_pict['din_code'] = json_obj['din_code']
    ingredient_dict = dict()
    print(json_obj['ingredient'])
    # mkp.add_new_pill()
    return 'Wrong address at FMP Root Dir'


@app.route('/grep_all', methods=['GET'])
def grep_all_from_db():
    all_data = dbm.connection_tester()
    print(str(all_data))
    return jsonify(all_data)


@app.route('/remove_pill', methods=['POST'])
def remove_pill():
    param = request.get_json()
    return 'Hello, FMP Team!' + do_this()


@app.route('/echo_call/<param>')
def get_echo_call(param):
    return jsonify({"param": param})


@app.route('/echo_call', methods=['POST'])  # post echo api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)


def do_this():
    print("ABCD")
    return "_+_Additional Return Val"


if __name__ == "__main__":
    app.run(host="localhost", port=9000, debug=True)
