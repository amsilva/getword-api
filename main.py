from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_message():
    return jsonify(palavra="GOIABA")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)