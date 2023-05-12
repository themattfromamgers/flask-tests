from flask import Flask, request

app = Flask(__name__)

@app.route('/createUser', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return 'Giriş başarılı!'

if __name__ == '__main__':
    app.run()
