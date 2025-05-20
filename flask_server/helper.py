from database_functions import add_flight


def main():
    dest = input("desination: ")
    dep = input("departure: ")
    row = int(input("rows: "))
    add_flight(dest, dep, row)


if __name__ == "__main__":
    main()
