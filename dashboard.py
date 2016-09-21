from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

idx_val = 0

@app.before_request
def before_request():
    if request.path != '/':
        if request.headers['content-type'].find('application/json'):
            return 'Unsupported Media Type', 415

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')}
    return jsonify(ret_data)
 
@app.route('/idx/', methods=['GET'])
def idx():
    global idx_val
    idx_val += 1
    ret_data = {"value": idx_val}
    return jsonify(ret_data)
 
@app.route('/reset/', methods=['GET'])
def reset():
    global idx_val
    idx_val = 0
    ret_data = {"value": idx_val}
    return jsonify(ret_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
