def main():
    """this function collecting the champions and how many times they have won
   and the countries of the champions in alphabetical order."""
    filename = "wimbledon.csv"
    information = turn_to_list(filename)
    times_wins = count_times_champions_win(information)
    countries = get_champions_countries(information)
    display_all_results(times_wins, countries)


def turn_to_list(filename):
    """turn the file into a list"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(",") for line in in_file.readlines()]


def count_times_champions_win(information):
    """count the number about how many times that champion won"""
    times_wins = {}
    for row in information[1:]:
        champion = row[2]
        if champion in times_wins:
            times_wins[champion] += 1
        else:
            times_wins[champion] = 1
    return times_wins


def get_champions_countries(information):
    """know the champions countries"""
    countries = {row[1] for row in information[1:]}
    return sorted(countries)


def display_all_results(times_wins, countries):
    """this function will display all the results"""
    print("Wimbledon Champions: ")
    for champions, wins in times_wins.items():
        print(f"{champions} {wins}")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()


