from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    a = {'name': 'aq', 'surname': 'addfsd', "age": 31}
    return jsonify(a)

if __name__ == "__main__":
  app.run(debug=True)