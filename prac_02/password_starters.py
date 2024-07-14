"""
this program will ask the user for a password, with error-checking to repeat
if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the password.
"""


def main():
    minimum_length = int(input("Minimum length: "))
    password = get_password()
    while len(password) < minimum_length:
        print(f"Please enter at least {minimum_length} digits.")
        password = get_password()
    #     ask user to enter the password again if the length of password is not enough
    print_the_asterisks(password)


def print_the_asterisks(password):
    print("*" * len(password))
# print asterisks as long as the word


def get_password():
    password = input("Password: ")
    return password


main()
