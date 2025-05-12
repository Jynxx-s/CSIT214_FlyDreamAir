import database_functions as dbf
from flask import Blueprint, jsonify, render_template, request

register_user_bp = Blueprint("register_user", __name__)


@register_user_bp.route("/register_user", methods=["POST"])
def register():
    """
    data = {
    "username" : "<username>",
    "email" : "<email>",
    "password" : "<password>"
    }
    """
    data = request.get_json()

    if dbf.user_exists(data["username"]):
        return jsonify({"message": "username already in use"})
    dbf.add_user(data["username"], data["password"], data["email"])
    return jsonify({"message": f"User {data['username']} registered!"}), 201


@register_user_bp.route("/")
def register_home():
    return render_template("register.html")
