from flask import Flask, jsonify, render_template, request
from datetime import datetime

app = Flask(__name__)

idx = 0

@app.before_request
def before_request():
    if request.path != '/':
        if request.headers['content-type'].find('application/json'):
            return 'Unsupported Media Type', 415

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/get_next_idx/', methods=['GET'])
def get_next_idx():
    global idx
    idx += 1
    ret_data = {"value": idx, "ts": datetime.now().strftime("%Y_%d_%m (%a) - %H:%M:%S.%f")[:-3]}
    return jsonify(ret_data)
 
@app.route('/reset_idx/', methods=['GET'])
def reset_idx():
    global idx
    idx = 0
    ret_data = {"value": idx}
    return jsonify(ret_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
