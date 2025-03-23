""""

All data base functions go here V

add_to_json : this takes one arguments and will attempt to add it to the json file

create_db : has no arguments will create the initial state of the database 
and clear if it has any data

"""







import json
import os

# gets the path for database file
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")


def add_to_json(data):

    with open(DB, 'r+') as f:
        file_data = json.load(f)
        file_data["bookingDetails"].append(data)
        f.seek(0)
        json.dump(file_data, f, indent=4)
        
    

def create_db():
    x = input("WARNING: this will clear the json file (y/n) to continue: ")
    if x.lower() == "n":
        return 
    
    # initial state for database
    dbdata = {
        "bookingDetails" :[

        ]

    }
    print(DB)
    with open(DB, "w") as f:
        json.dump(dbdata, f, indent=4)

if __name__ == "__main__":
    create_db()
