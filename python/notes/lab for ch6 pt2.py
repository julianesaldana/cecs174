"""
Write a program that takes a string as input:

    Enter a string :

and display

    Only uppercase letters in the string :

    Every second letter/number in the string:

    Replacing all the vowels with underscore:

    The total number of digits in the string:

then lastly display

    The positions of all the vowels in the string:

if text[i].isalnum():
       print(text[i], end="")
"""
text = input("Enter a string: ")
vowels = ["a", "e", "i", "o", "u"]
counter = 0

print("Only upper case letters in the string: ", end="")
for i in range(len(text)):
    if text[i].isupper():
        print(text[i], end="")
print()
print("Every second letter/number in the string: ", end="")
for i in range(1, len(text), 2):
    print(text[i], end="")
print()
print("Replacing all the vowels with underscore: ", end="")
for i in range(len(text)):
    if (text[i]).lower() in vowels:
        print(text[i].replace(text[i], "_"), end="")
    else:
        print(text[i], end="")
print()
print("The total number of digits in the string: ", end="")
for i in range(len(text)):
    if text[i].isdigit():
        counter += 1
print(counter)
print("The positions of all the vowels in the string: ", end="")
for i in range(len(text)):
    if text[i].lower() in vowels:
        print(i, end=" ")


