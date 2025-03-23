import json
import os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")
def add_to_json(data):

    with open(DB, 'w') as f:
       json.dump(data, f, indent=4)
       print("hello")
    