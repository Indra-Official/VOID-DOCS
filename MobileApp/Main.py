# Importing necessary modules from Flask and other files
from flask import Flask, render_template, request, session
from Logined import logined          # Custom function to check login credentials
from Registeration import registeration  # Custom function to handle registration
from dontcommit import MongoDB
# Create a Flask web app
app = Flask(__name__)

# Connect to MongoDB (replace MongoDB with your unique access string)
x = MongoDB

# -------------------------------------------
# ROUTE 1: Home Page
# -------------------------------------------
@app.route('/')
def home():
    # When the user visits the base URL, render 'index.html'
    return render_template('index.html')


# -------------------------------------------
# ROUTE 2: Login Page (GET)
# -------------------------------------------
@app.route('/Login', methods=['POST', 'GET'])
def Login():
    # Shows the login form page (Login.html)
    return render_template('Login.html')


# -------------------------------------------
# ROUTE 3: Handle Login Form Submission (POST)
# -------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the form is submitted
    if request.method == 'POST':
        # Get data entered by the user from the form
        user_id = request.form['user_id']
        user_pass = request.form['password']

        # Call the 'logined' function to check credentials
        # It returns a message and login status (True/False)
        m = logined(user_id, user_pass, x)
        msg = m[0]
        Login_status = m[1]

        # If login successful, go to Home page
        if Login_status:
            return render_template('Home.html')
        # If login failed, show the login page again with an error message
        else:
            return render_template('Login.html', message=msg)
    
    # If accessed via GET (not submitting form), just show login page
    return render_template('Login.html')


# -------------------------------------------
# ROUTE 4: Register Page (GET)
# -------------------------------------------
@app.route('/Register', methods=['POST', 'GET'])
def Register():
    # Shows the registration form page (Register.html)
    return render_template('Register.html')


# -------------------------------------------
# ROUTE 5: Handle Registration Form Submission (POST)
# -------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""  # Default message

    # If user submitted the registration form
    if request.method == 'POST':
        # Get data from the registration form
        name = request.form['name']
        user_id = request.form['user_id']
        user_pass = request.form['password']

        # Call the 'registeration' function to register the user
        # It returns a message and registration status
        m = registeration(name, user_id, user_pass, x)
        msg = m[0]
        Register_status = m[1]

        # If registration successful, go to Home page
        if Register_status:
            return render_template('Home.html')
        # If registration failed, reload registration page with message
        else:
            return render_template('Register.html', message=msg)
    
    # If accessed via GET, just show the registration page
    return render_template('Register.html')


# -------------------------------------------
# Run the Flask web app
# -------------------------------------------
if __name__ == '__main__':
    # debug=True allows auto-reload when you make code changes
    app.run(debug=True)
