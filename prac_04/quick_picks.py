"""
This program is to generates that many lines of output. Each line consists of 6 random numbers between 1 and 45
"""
import random

NUM_NUMBERS = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45
try:
    num_quick_picks = int(input("How many quick picks? "))
    for i in range(num_quick_picks):
        for j in range(NUM_NUMBERS):
            number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
            print(f"{number:2}", end = " ")
        print()
except SyntaxError:
    num_quick_picks = int(input("How many quick picks? "))
except ValueError:
    num_quick_picks = int(input("How many quick picks? "))
