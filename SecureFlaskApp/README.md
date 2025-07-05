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

Project Structure
-----------------
SecureFlaskApp/
├── app.py
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
├── static/
├── screenshots/
│   ├── step0.png
│   ├── step1.png
│   ├── step2.png
│   └── step3.png
├── venv/
└── README.md

Setup Instructions
------------------
1. Clone or create the folder:

    mkdir SecureFlaskApp
    cd SecureFlaskApp

2. Create a virtual environment:

    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies:

    pip install flask flask_sqlalchemy flask_wtf

4. Run the app:

    python3 app.py

5. Visit in browser:

    http://127.0.0.1:5000

Screenshots
-----------
- screenshots/step0.png – Project setup
- screenshots/step1.png – Flask app code
- screenshots/step2.png – HTML templates
- screenshots/step3.png – App running in browser
