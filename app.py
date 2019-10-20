from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    fabs = ['john', 'paul', 'george', 'ringo', 'BILLY PRESTON']
    return jsonify({'fabs': fabs})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')