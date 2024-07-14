"""
This program is allows a user to enter a name and get the code
"""
HEX_TO_COLOURS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                  "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "Antique White": "#faebd7", "Antique White1": "#ffefdb", "Antique White2": "#eedfcc"}
print(HEX_TO_COLOURS)
colour_names = []
colour_name = input("Enter colour name (or blank to quit): ").title().strip()
while colour_name:
    try:
        print(f"Hex of {colour_name} is {HEX_TO_COLOURS[colour_name]}")
        colour_names.append(colour_name)
    except KeyError:
        print("Invalid input")
    colour_name = input("Enter colour name (or blank to quit): ").title().strip()
for colour_name in colour_names:
    print(f"hex of {colour_name:16} is {HEX_TO_COLOURS[colour_name]}")

