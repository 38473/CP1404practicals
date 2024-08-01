from unreliable_car import UnreliableCar


def main():
    """test the unreliableCar class"""
    unreliable_car = UnreliableCar("new car", 100, 60)
    print(unreliable_car)
    for i in range(5):
        distance_driven = unreliable_car.drive(20)
        print(f"drives {distance_driven}km")
        print(unreliable_car)


if __name__ == '__main__':
    main()
