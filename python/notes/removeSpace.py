userInput = input("Enter a string:")
print("The new string:", end=" ")
for letter in range((len(userInput)-1), -1, -1):
    if userInput[letter] != ' ':
        print(userInput[letter], end="")
