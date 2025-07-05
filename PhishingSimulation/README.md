
# Phishing Awareness Simulation

## Description

This project simulates a phishing campaign using a local Flask server to help raise awareness about common social engineering tactics. It demonstrates how a phishing email and landing page might appear, without sending any real emails.

## Features

- Simulated phishing login page
- Captures and prints submitted credentials (locally)
- Educational and ethical use only
- Ideal for cybersecurity awareness training

## Usage

### Step 0: Set Up Project Folder

```
mkdir PhishingSimulation
cd PhishingSimulation
python3 -m venv venv
source venv/bin/activate
```

### Step 1: Install Required Library

```
pip install flask
```

### Step 2: Create the Flask App

```
nano phishing_app.py
```

Paste the following code:

```python
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <h2>Your Account Needs Verification!</h2>
    <p>We detected suspicious activity. Please log in to verify your account.</p>
    <form action="/submit" method="POST">
        Email: <input name="email" type="email"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Verify Now">
    </form>
    """)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    print(f"[!] Caught credentials → Email: {email} | Password: {password}")
    return "<h3>Thank you! Your account is verified.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### Step 3: Run the Simulation

```
python3 phishing_app.py
```

Visit `http://localhost:8080` in your browser. Try entering test credentials — they will print to the terminal for demonstration.

## Screenshots

- step0.png – Project folder and virtual environment setup
- step1.png – pip install flask
- step2.png – Editing `phishing_app.py`
- step3.png – Web browser showing the phishing login form

## Folder Structure

```
PhishingSimulation/
├── screenshots/
│   ├── step0.png
│   ├── step1.png
│   ├── step2.png
│   └── step3.png
├── phishing_app.py
└── README.md
```

## Disclaimer

**For educational and ethical use only.**  
This is a local simulation meant for awareness training and responsible use in controlled environments.

## License

MIT – Free to use and modify.
