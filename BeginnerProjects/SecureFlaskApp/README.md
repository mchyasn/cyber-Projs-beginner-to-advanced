Secure Flask Web App
=====================

This is a simple secure web application built using Python's Flask framework. It demonstrates secure login and registration, session handling, password hashing, and CSRF protection.

Features
--------
- User registration with password hashing
- User login and session management
- CSRF protection using Flask-WTF
- Basic SQLite database using SQLAlchemy
- Secure coding practices: input validation, error handling

------------------
1. Clone or create the folder:

    mkdir SecureFlaskApp
    cd SecureFlaskApp

2. Create a virtual environment:

    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies:

    pip install flask flask_sqlalchemy flask_wtf

   ![Secure Flask Login](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/SecureFlaskApp/screenshots/Screenshot%202025-07-05%20101219.png)

4. Create templates/ with:

index.html

register.html

login.html

dashboard.html

![Flask Admin Dashboard](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/SecureFlaskApp/screenshots/Screenshot%202025-07-05%20101700.png)

5. create the file , Run the app:
![Flask User Dashboard](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/SecureFlaskApp/screenshots/Screenshot%202025-07-05%20101318.png)
```bash
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user'] = user.username
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

```

   name it as python3 app.py 
   
6. Visit in browser:
    http://127.0.0.1:5000
Register a new user (test credentials like admin / adminpass).

Login and test the dashboard.
![Flask Security Features](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/SecureFlaskApp/screenshots/Screenshot%202025-07-05%20102402.png)


