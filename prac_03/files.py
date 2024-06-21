name = input("Name: ")
out_file = open("name.txt", "w")
while name != "":
    out_file.write(name + "\n")
    name = input("Name: ")
out_file.close()

in_file = open("name.txt", "r")
print(in_file.read())
in_file.close()
print("Hi Bob!")

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
result = first_number + second_number
print(result)

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line.strip())
print(total)
