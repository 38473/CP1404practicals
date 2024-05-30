minimum_length = int(input("Minimum length: "))
password = input("Password: ")
while len(password) < minimum_length:
    print(f"Please enter at least {minimum_length} digits.")
    password = input("Password: ")
print("*" * len(password))