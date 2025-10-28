from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Login', methods=['POST','GET'])
def Login():
    return render_template('Login.html')

@app.route('/Register', methods=['POST','GET'])
def Register():
    return render_template('Register.html')


if __name__ == '__main__':
    app.run(debug=True)
