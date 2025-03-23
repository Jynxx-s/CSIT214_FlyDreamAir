from flask import Flask, render_template, request
from loyalty import loyalty_bp
from booking import booking_bp
import requests as rqst
import csv

app = Flask(__name__, template_folder='../templates', static_folder='../static')


app.register_blueprint(loyalty_bp, url_prefix='/loyalty')
app.register_blueprint(booking_bp, url_prefix='/booking')


@app.route('/')
def home():
    return render_template('home.html')




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)