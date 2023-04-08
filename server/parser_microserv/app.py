from flask import Flask, jsonify
from flask_cors import CORS
from main import *

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/parser/start_all', methods=['GET', 'POST'])
def index():
    main()
    return jsonify({"status": 200})

if __name__ == '__main__':
    app.run(port = 3444, debug = True)