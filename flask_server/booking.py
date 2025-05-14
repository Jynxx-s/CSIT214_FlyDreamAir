from flask import Blueprint, render_template, request, jsonify
import database_functions as dbf
from login import login_required

booking_bp = Blueprint('booking', __name__)


@booking_bp.route('/')
@login_required
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

    dbf.add_to_booking(data)
    
    return jsonify({"message" : "it worked"}), 200


@booking_bp.route('/get_flights', methods=["GET"])
def get_flights():
    flights = dbf.get_flights()
    return jsonify({"flights" : flights})
