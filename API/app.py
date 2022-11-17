from flask import Flask, request, jsonify
import db_communicate as dbm

app = Flask(__name__)


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


def do_this():
    print("ABCD")
    return "_+_Additional Return Val"


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
