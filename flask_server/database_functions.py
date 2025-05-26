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



def create_db():
    x = input("WARNING: this will clear the json file (y/n) to continue: ")
    if x.lower() == "n":
        return

    # initial state for database
    dbdata = {
        "bookingDetails": [],
        "users": [],
        "flights": [],
        "nextFlightId": 0,
        "nextBookingId": 0,
    }
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
            flights.append({"destination": i["destination"], "depart": i["depart"], "flight_id": i["flight_id"]})
    return flights


def get_next_flight_id():
    with open(DB, "r") as f:
        file_data = json.load(f)
        file_data["nextFlightId"] += 1
        with open(DB, "w") as f:
            json.dump(file_data, f, indent=4)
        return file_data["nextFlightId"] - 1


def add_flight_booking(flight_id, username, email, seats):
    """
    booking :
    {
        booking_id : <booking_id>,
        flight_id : <flight_id>,
        seats : ["a1", "a2", "a3", "b1", "b2", "b3"],
        username : "<username>",
        email : "<email>",
    }
    """
    booking_id = get_next_booking_id()
    data = {
        "booking_id": booking_id,
        "flight_id": flight_id,
        "username": username,
        "email": email,
        "seats": seats,
    }
    with open(DB, "r+") as f:
        file_data = json.load(f)
        file_data["bookingDetails"].append(data)

        f.seek(0)
        json.dump(file_data, f, indent=4)


def get_next_booking_id():
    with open(DB, "r+") as f:
        file_data = json.load(f)
        file_data["nextBookingId"] += 1
        next_id = file_data["nextBookingId"]

        f.seek(0)
        json.dump(file_data, f, indent=4)
        f.truncate()

    return next_id - 1

def add_flight(destination, depart, rows):
    """
    flight data:
    {
        flight_id : <id>,
        destination : "<destination>",
        depart : "<depart>",

        "seats": [
            {"a1": "a", "a2": "a", "a3": "a", "a4": "a", "a5": "a", "a6": "a"},
            {"b1": "a", "b2": "a", "b3": "a", "b4": "a", "b5": "a", "b6": "a"},
            {"c1": "a", "c2": "a", "c3": "a", "c4": "a", "c5": "a", "c6": "a"},
            {"d1": "a", "d2": "a", "d3": "a", "d4": "a", "d5": "a", "d6": "a"},
            {"e1": "a", "e2": "a", "e3": "a", "e4": "a", "e5": "a", "e6": "a"},
            {"f1": "a", "f2": "a", "f3": "a", "f4": "a", "f5": "a", "f6": "a"}
        ]
    }
    """
    id = get_next_flight_id()
    seats = [{f"{chr(97 + i)}{j+1}": "a" for j in range(6)} for i in range(rows)]
    data = {
        "flight_id": id,
        "destination": destination,
        "depart": depart,
        "seats": seats,
    }
    with open(DB, "r+") as f:
        file_data = json.load(f)
        file_data["flights"].append(data)
        f.seek(0)
        json.dump(file_data, f, indent=4)

def get_email(username):
    with open(DB, "r") as f:
        file_data = json.load(f)
        for i in file_data["users"]:
            if i["username"] == username:
                return i["email"]

def get_seats(flight_id):
    with open(DB, "r") as f:
        file_data = json.load(f)
        for i in file_data["flights"]:
            if i["flight_id"] == flight_id:
                return i["seats"]
def mark_seats_unavailable(flight_id, selected_seats):
    with open(DB, "r+") as f:
        file_data = json.load(f)
        for flight in file_data["flights"]:
            if flight["flight_id"] == flight_id:
                for row in flight["seats"]:  # row is a dict
                    for seat in row:
                        if seat in selected_seats:
                            row[seat] = "u"    

        f.seek(0)
        json.dump(file_data, f, indent=4)
        f.truncate()


if __name__ == "__main__":
    create_db()
