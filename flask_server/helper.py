from database_functions import add_flight, add_user 


def fill_db():

    add_flight("USA", "AUS", 8)
    add_flight("CHI", "SYD", 10)
    add_user("admin", "admin", "admin@flydreamair.com")

if __name__ == "__main__":
    fill_db()
