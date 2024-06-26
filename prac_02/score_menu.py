"""
This program determines score status and prints stars as many as the score.
"""
MENU = ("(G)et a valid score (must be 0-100 inclusive)\n"
        "(P)rint result (copy or import your function to determine the result from score.py)\n"
        "(S)how stars (this should print as many stars as the score)\n"
        "(Q)uit")


def main():
    score = get_valid_score()
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = output_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Thank you for your use! Goodbye!")


def show_stars(score):
    print("*" * int(score))


def output_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
