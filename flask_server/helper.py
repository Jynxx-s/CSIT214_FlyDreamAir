from database_functions import add_flight 


def main():
    dest = input("desination: ")
    dep = input("departure: ")
    row = int(input("rows: "))
    cols = int(input("columns: "))
    add_flight(dest, dep, row, cols)


if __name__ == "__main__":
    main()
