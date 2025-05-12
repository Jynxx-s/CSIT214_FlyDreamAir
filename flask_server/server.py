from flask import Flask, render_template, redirect, url_for, session, request
from booking import booking_bp
from register_user import register_user_bp
import requests as rqst

from login import login_required
import database_functions as dbf

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.register_blueprint(booking_bp, url_prefix='/booking')
app.register_blueprint(register_user_bp, url_prefix='/register')
app.secret_key = "123"






@app.route('/home')
@login_required
def home():
    return render_template('home.html')
  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if dbf.attempt_login(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')  # Render the login page for GET requests

@app.route('/')
def base():
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
