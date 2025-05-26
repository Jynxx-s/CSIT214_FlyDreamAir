import database_functions as dbf
from flask import Blueprint, jsonify, render_template, request, session
from login import login_required

booking_bp = Blueprint("booking", __name__)


@booking_bp.route("/")
@login_required
def booking_home():
    return render_template("booking.html")


@booking_bp.route("/create_booking", methods=["POST"])
def create_booking():
    data = request.get_json()

    dbf.add_flight_booking(data["flight_id"], session["username"], session["email"], data["seats"])
    return jsonify({"message": "Thank you for booking"}), 200





@booking_bp.route("/get_flights", methods=["GET"])
def get_flights():
    flights = dbf.get_flights()
    return jsonify({"message": flights}), 200
