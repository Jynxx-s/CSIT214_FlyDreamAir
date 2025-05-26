import database_functions as dbf
from flask import Blueprint, jsonify, render_template, request, session
from login import login_required

booking_bp = Blueprint("booking", __name__)


@booking_bp.route("/")
@login_required
def booking_home():
    return render_template("booking.html")


@booking_bp.route("/manage")
@login_required
def booking_manage():
    return render_template("manage_booking.html")


@booking_bp.route("/create_booking", methods=["POST"])
def create_booking():
    data = request.get_json()

    dbf.add_flight_booking(
        int(data["flight_id"]), session["username"], session["email"], data["seats"]
    )
    dbf.mark_seats_unavailable(int(data["flight_id"]), data["seats"])
    return jsonify({"message": "Thank you for booking"}), 200


@booking_bp.route("/get_flights", methods=["GET"])
def get_flights():
    flights = dbf.get_flights()
    return jsonify({"message": flights}), 200


@booking_bp.route("/get_seats", methods=["POST"])
def get_seats():
    data = request.get_json()
    seats = dbf.get_seats(int(data["flight_id"]))

    return jsonify({"message": seats}), 200


@booking_bp.route("get_bookings", methods=["GET"])
def get_booking():
    bookings = dbf.get_bookings(session["username"])
    return jsonify({"message": bookings}), 200


@booking_bp.route("delete_booking", methods=["POST"])
def delete_booking():
    data = request.get_json()
    dbf.delete_booking(int(data["booking_id"]))
    return jsonify({"message": "deleted"}), 204













