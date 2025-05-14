""" "

All data base functions go here V

add_to_json : this takes one arguments and will attempt to add it to the json file

create_db : has no arguments will create the initial state of the database
and clear if it has any data

"""

import json
import os

# gets the path for database file
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")


def add_to_booking(data):

    with open(DB, "r+") as f:
        file_data = json.load(f)
        file_data["bookingDetails"].append(data)
        f.seek(0)
        json.dump(file_data, f, indent=4)


def create_db():
    x = input("WARNING: this will clear the json file (y/n) to continue: ")
    if x.lower() == "n":
        return

    # initial state for database
    dbdata = {"bookingDetails": [], "users": [], "flights": []}
    print(DB)
    with open(DB, "w") as f:
        json.dump(dbdata, f, indent=4)


def user_exists(username):
    with open(DB, "r") as f:
        file_data = json.load(f)
        for user in file_data["users"]:
            if user["username"] == username:
                return True
    return False


def add_user(username, password, email):

    with open(DB, "r+") as f:
        file_data = json.load(f)
        data = {"username": username, "password": password, "email": email}
        file_data["users"].append(data)
        f.seek(0)
        json.dump(file_data, f, indent=4)


def attempt_login(username, password):
    with open(DB, "r") as f:
        file_data = json.load(f)
        for i in file_data["users"]:
            if i["username"] == username and i["password"] == password:
                return True
    return False


def get_flights():
    flights = []
    with open(DB, "r") as f:
        file_data = json.load(f)
        for i in file_data["flights"]:
            flights.append({"destination": i["destination"], "depart": i["depart"]})
        return flights


def add_flight(destination, depart, rows, cols):
    """
    flight data:
    {
    destination : "<destination>",
    depart : "<depart>",
    seats : "<[
        [a1, a2, a3, a4, a5, a6],
        [b1, b2, b3, b4, b5, b6],
        [c1, c2, c3, c4, c5, c6],
        [d1, d2, d3, d4, d5, d6],
        [e1, e2, e3, e4, e5, e6],
        [f1, f2, f3, f4, f5, f6]
    ]>"

    }
    """

    seats = (
        lambda r, c: [[f"{chr(97 + i)}{j+1}" for j in range(c)] for i in range(r)]
    )(cols, rows)
    data = {"destination": destination, "depart": depart, "seats": seats}
    with open(DB, "r+") as f:
        file_data = json.load(f)
        file_data["flights"].append(data)
        f.seek(0)
        json.dump(file_data, f, indent=4)


if __name__ == "__main__":
    create_db()
