from flask import Flask, request, jsonify
import db_communicate as dbm
import sys

app = Flask(__name__)


@app.route('/')
def wrong_addr_at_root_dir():
    return 'Wrong address at FMP Root Dir'


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
    dbm.connection_tester()
    app.run(host="localhost", port=8000, debug=True)
