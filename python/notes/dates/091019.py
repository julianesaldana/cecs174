""" for lab 4 ch.14
response = input("Enter the string with $: ")
for i in range (len(response)-1, -1, -1):   #method 1
    if response[i] != "$"
        print(response[: i + 1])
        break

while response.endswith("$"):
    response = response[:len(response)-1]   #method 2
print(response)
"""

"""
IF STATEMENTS:
if 'variable' == 1:
    print('whatever')
elif:
    print('whatever')
else:
    print('whatever')

"""
"""
word = input("Enter a word: ")
if word.isalpha() == True:
    print("The word contains only letters.")
if word.isupper() == True:
    print("All string in the word are uppercase letters.")
if word.islower() == True:
    print("All string in the word are lowercase letters.")
if word.isnumeric() == True:
    print("The word contains only digits.")
if word.isalnum() == True:
    print("The word contains either letters or numbers.")
if word[0].isupper() == True:
    print("The word starts with a capital letter.")
if word[-1].endswith('.') == True:
    print("The word ends with a period.")
"""

user_grade = input("Enter a letter grade: ").capitalize()
if user_grade[0] == 'A':
    numericValue = 4.0
elif user_grade[0] == 'B':
    numericValue = 3.0
elif user_grade[0] == 'C':
    numericValue = 2.0
elif user_grade[0] == 'D':
    numericValue = 1.0
elif user_grade[0] == 'F':
    numericValue = 0.0

if numericValue != 0.0:
    if len(user_grade) == 2:
        if user_grade[1] == '+' and numericValue != 4.0:
            numericValue = numericValue + 0.3
        elif user_grade[1] == '-':
            numericValue = numericValue - 0.3

print("The numeric value is", numericValue)

