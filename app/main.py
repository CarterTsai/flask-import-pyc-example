from flask import Flask, jsonify
from lib.test import Animal

app = Flask(__name__)


@app.route("/")
def hello():
    x = Animal("dog")
    return jsonify({'who': x.who()})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
