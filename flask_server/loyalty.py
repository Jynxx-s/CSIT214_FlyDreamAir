from flask import Blueprint, render_template, request, jsonify
import database_functions as dbf

loyalty_bp = Blueprint('loyalty', __name__)


@loyalty_bp.route('/')
def loyalty_home():
    return render_template('loyalty.html')


@loyalty_bp.route('/signup', methods=['POST'])
def loyalty_signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    data = {
        'username' : username,
        'email' : email,
        'password' : password
    }

    if dbf.user_exists(username):
        return jsonify({"message" : "user already exists"}), 400
    dbf.add_user(data)
    return jsonify({"message" : "Registered"}), 200