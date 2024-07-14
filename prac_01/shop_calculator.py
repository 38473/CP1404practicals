total = 0
discount = 0.1
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for item in range(0, number):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total = total * (1 - discount)
print(f"Total price for {number} items is ${total:.2f}")

