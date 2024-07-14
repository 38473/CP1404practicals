"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = output_result(score)
    print(result)
    random_score = generate_random_score()
    random_result = output_result(random_score)
    print(f"The random score is {random_score} and the result of random score is {random_result}")


def generate_random_score():
    random_score = random.randint(0, 100)
    # generate random score from 0 to 100
    return random_score


def output_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
