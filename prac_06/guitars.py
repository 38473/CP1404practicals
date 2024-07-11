from guitar import Guitar


def main():
    """use a list to store all the user's guitars"""
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40)]
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")
    guitars = sorted(guitars, key=lambda guitar: guitar.year)
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            tag = "(vintage)"
        else:
            tag = ""
        print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f}{tag}")


main()
