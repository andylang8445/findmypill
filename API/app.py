from flask import Flask, request, jsonify
import db_communicate as dbm
import search_handler as searcher

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def wrong_addr_at_root_dir():
    return 'Wrong address at FMP Root Dir'


@app.route('/grep_all', methods=['GET'])
def grep_all_from_db():
    all_data = dbm.connection_tester()
    print(str(all_data))
    return jsonify(all_data)


@app.route('/hello')
def hello_world():
    return 'Hello, FMP Team!' + do_this()


@app.route('/echo_call/<param>')
def get_echo_call(param):
    return jsonify({"param": param})


@app.route('/echo_call', methods=['POST'])  # post echo api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)


@app.route('/search', methods=['POST'])
def search_from_db():
    param = request.get_json()
    request_type = param['search_criteria']
    request_data = param['search_data']
    pill_cnt = int
    pill_data = list()
    if request_type == 'DIN':
        pill_cnt, pill_data = searcher.search_by_din(request_data)
    elif request_type == 'Company':
        pass
        # search for given company name
    elif request_type == 'Name':
        # search by pill name
        pass
    elif request_type == 'Ingredient':
        # search by pill ingredient
        pass
    else:
        # unknown request
        pass


def do_this():
    print("ABCD")
    return "_+_Additional Return Val"


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
