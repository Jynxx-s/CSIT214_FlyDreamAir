from flask import Blueprint, render_template, request, jsonify
import database_functions as dbf

booking_bp = Blueprint('booking', __name__)


@booking_bp.route('/')
def booking_home():
    return render_template('booking.html')


       
     

@booking_bp.route('/create_booking', methods=['POST'])
def create_booking():
    name = request.form.get('name')
    email = request.form.get('email')
    snum = request.form.get('snum')

    data = {
        'name' : name,
        'email' : email,
        'snum' : snum
    }

    dbf.add_to_json(data)
    
    return jsonify({"message" : "it worked"}), 200
