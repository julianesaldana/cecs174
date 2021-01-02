"""
file_name = input("Enter the name of a file:")
infile = open(file_name, "r")
contents = infile.read().strip().upper()
alphabet = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
            "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

for i in range(len(contents)):
    if contents[i] in alphabet:
        alphabet[contents[i]] += 1

for alpha, value in alphabet.items():
    if value != 0:
        print(alpha, format(value / len(contents) * 100, ".2f") + "%")
"""

user_file = input("Enter the name of a file:")
infile = open(user_file, "r")
contents = infile.read().strip().
print(contents)
