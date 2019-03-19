from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy

DB_URL = 'postgresql://postgres:Welcome@123@127.0.0.1:5432/userdata'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Welcome@123'

db = SQLAlchemy(app)

from user_model import UserAuthentication


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def welcome():
    return render_template('welcome.html')

# let's prompt user to login by email
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        # retrieve stored user email and password from db
        user_email = UserAuthentication.check_email(['email'])
        user_password = UserAuthentication.fetch_user(['password'])
        
        # check if email and password equal to the stored credentials
        if email != user_email:
            flash("Email does not exist please register")
            return redirect(url_for('register'))
        
        if email == user_email and password =!user_password:
            flash("Wrong Password!") 
            return redirect(url_for('login'))
        
        if email == user_email and password == user_password:
            flash("Successfully Logged In")
            return redirect(url_for('welcome'))
            
    return render_template('login.html')



# render the register function which will create a user
@app.route('/register', methods=['POST', 'GET'])
def add_new_user():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # check if passwords match
        if password != confirm_password:
            flash('Passwords do not match')
            return render_template('register.html')

        # check if email already exists since email should be unique
        # call the function check_email defined in user_model to do this
        if UserAuthentication.check_email(email):
            flash("Email already registered")
            return render_template('register.html')

        # if user meets all conditions create new user
        else:
            register = UserAuthentication(firstname=firstname, lastname=lastname, email=email, password=password)
            register.create_user()
            flash("successfully registered")
            return redirect(url_for('login'))
    else:
        return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
