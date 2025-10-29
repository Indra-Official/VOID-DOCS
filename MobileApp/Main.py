from flask import Flask, render_template, request , session
from Logined import logined
from Registeration import registeration
from dontcommit import MongoDB

app = Flask(__name__)
x = MongoDB

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Login', methods=['POST','GET'])
def Login():
    return render_template('Login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pass = request.form['password']

        m = logined(user_id, user_pass, x)
        msg = m[0]
        Login_status = m[1]

    if Login_status:
        return render_template('Home.html')
    else:
        return render_template('Login.html', message = msg)

@app.route('/Register', methods=['POST','GET'])
def Register():
    return render_template('Register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == 'POST':
        name = request.form['name']
        user_id = request.form['user_id']
        user_pass = request.form['password']

    m = registeration(name, user_id, user_pass, x)
    Register_status = m[1]
    msg = m[0]

    if Register_status:
        return render_template('Home.html')
    else:
        return render_template('Register.html', message = msg)

if __name__ == '__main__':
    app.run(debug=True)
