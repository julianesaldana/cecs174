userInput = input("Enter a sequence of comma-separated numbers:").split(",")
if userInput[0].isnumeric():
    for number in range(len(userInput)):
        if (int(userInput[number]) % 2) != 0:
            if userInput[number] == userInput[-1]:
                print(userInput[number])
            elif userInput[number] != userInput[-1]:
                if userInput[number+1] == userInput[-1]:
                    print(userInput[number])
                else:
                    print(userInput[number], end=",")