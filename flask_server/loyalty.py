from flask import Blueprint, render_template

loyalty_bp = Blueprint('loyalty', __name__)


@loyalty_bp.route('/')
def loyalty_home():
    return render_template('loyalty.html')