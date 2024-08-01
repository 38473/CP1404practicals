from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    MENU = """q)uit, c)hoose taxi, d)rive"""
    print(MENU)
    while True:
        choice = input(">>> ").lower()
        if choice == "q":
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)


def choose_taxi(taxis, current_taxi):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return current_taxi
    except (IndexError, ValueError):
        print("Invalid taxi choice")
        return current_taxi


def drive_taxi(current_taxi, total_bill):
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        try:
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            trip_cost = round(current_taxi.get_fare(), 1)
            total_bill += trip_cost
            total_bill = round(total_bill, 1)
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        except ValueError:
            print("Invalid distance")
    return total_bill


if __name__ == '__main__':
    main()
