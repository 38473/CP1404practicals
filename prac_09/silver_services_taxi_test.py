from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    new_taxi = SilverServiceTaxi("newtaxi", 100, 2)
    print(new_taxi)
    new_taxi.drive(18)
    assert new_taxi.get_fare() == 48.78


if __name__ == '__main__':
    main()
