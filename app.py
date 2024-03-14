from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'saygcsuAYgyvuggUUYGUgb8372R9724T4Y98U'

# Configure MySQL
app.config['MYSQL_HOST'] = 'sql.freedb.tech'
app.config['MYSQL_USER'] = 'freedb_new_user'
app.config['MYSQL_PASSWORD'] = 'VFkh!dFzfeMj3Y#'
app.config['MYSQL_DB'] = 'freedb_COMPANIONCARE'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=['GET'])
def register():
    return render_template("reg.html")

@app.route("/registersave", methods=['POST'])
def registersave():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    number = request.form.get('phone')
    qualification = request.form.get('jobtitle')
    password = request.form.get('passwordConfirmation')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user_details (first_name, last_name, email, phone_number, qualification, password) VALUES (%s, %s, %s, %s, %s, %s)", (firstname, lastname, email, number, qualification, password))
    mysql.connection.commit()
    cur.close()

    # Assuming the registration is successful
    return redirect('/dashboard')  # Redirect to dashboard after successful registration


@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/logincheck", methods=["POST","GET"])
def logincheck():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email, password)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cur.fetchone()
    cur.close()
    print(user)

    if user:
        session['loggedin'] = True
        session['email'] = email
        return redirect('/dashboard')
    else:
        return '''
        <script>
            alert("Login unsuccessfully");
        </script>
        ''' , redirect('/login')

@app.route("/dashboard")
def dashboard():
    if 'loggedin' in session:
        return render_template("dashboard.html", email=session['email'])
    else:
        return redirect('/login', code=302)
    
@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/work")
def work():
    return render_template("work profile.html")

@app.route("/personal")
def personal():
    return render_template("stress.html")

if __name__ == "__main__":
    app.run(debug=True)
