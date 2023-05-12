from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    bvak = 'iambuvak'
    return render_template('test.html', bvak=bvak)
@app.route('/deneme')
def deneme2():
  return "<h2>Denem2</h2>"

@app.route('/user')
def deneme():
    
    return redirect(url_for('deneme2'))

if __name__ == "__main__":
  app.run(debug=True)
