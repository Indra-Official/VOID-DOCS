from flask import Flask, render_template, request, session, redirect, url_for
from dontcommit import MongoDB, flask
from Login_Register import logined , registeration


app = Flask(__name__)
app.secret_key = flask

app = Flask(__name__)
app.secret_key = flask

x = MongoDB

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('Home'))
    else:
        return render_template('index.html')


@app.route('/Login_Page', methods=['POST', 'GET'])
def Login_Page():
    return render_template('Login.html')


@app.route('/Register_Page', methods=['POST', 'GET'])
def Register_Page():
    return render_template('Register.html')


@app.route('/Login_Admin', methods=['GET', 'POST'])
def Login_Admin():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pass = request.form['password']
        m = logined(user_id, user_pass, x)
        msg = m[0]
        Login_status = m[1]

        if Login_status:
            session['user_id'] = user_id
            return render_template('Home.html')
        else:
            return render_template('Login.html', message=msg)
    
    return render_template('Login.html')


@app.route('/Register_Admin', methods=['GET', 'POST'])
def Register_Admin():
    message = "" 
    
    if request.method == 'POST':
        
        name = request.form['name']
        user_id = request.form['user_id']
        user_pass = request.form['password']

        m = registeration(name, user_id, user_pass, x)
        msg = m[0]
        Register_status = m[1]

        if Register_status:
            session['user_id'] = user_id
            return render_template('Home.html')
        else:
            return render_template('Register.html', message=msg) 
    
    return render_template('Register.html')


@app.route('/Home')
def Home():
    if 'user_id' not in session:
        return redirect(url_for('Login'))
    return render_template('Home.html')


@app.route('/Download', methods=['POST','GET'])
def download_file(file_id, output_folder, collection):
    from bson import ObjectId

    try:
        # Ensure file_id is an ObjectId
        if isinstance(file_id, str):
            file_id = ObjectId(file_id)

        # Fetch document
        doc = collection.find_one({'_id': file_id})
        if not doc:
            return "File not found in MongoDB."

        filename = doc.get('filename', 'restored_file')
        file_data = doc.get('file_data')

        if not file_data:
            return "No file data found in document."

        # Save to disk
        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'wb') as f:
            f.write(file_data)

        return f"File restored to: {output_path}"

    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/Upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return 'No files uploaded', 400

    files = request.files.getlist('files[]')
    uploaded = []

    for file in files:
        if file.filename:
            file_data = file.read()  # Read file content as bytes
            file_hash = sha256_hasher(file)  # Compute hash

            document = {
                'filename': file.filename,
                'content_type': file.content_type,
                'file_data': bson.Binary(file_data),
                'sha256_hash': file_hash
            }
            client = MongoClient(x)
            db = client["VOID-Docs"]
            Documents = db["Documents"]

            result = Documents.insert_one(document)
            uploaded.append(str(result.inserted_id))

    return f"Files stored with IDs: {', '.join(uploaded)}"


@app.route('/Logout')
def Logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)