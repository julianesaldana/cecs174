ct = 0
userList = []
while ct < 5:
    userInput = float(input("Please enter a floating point number: "))
    if userInput not in userList:
        userList.append(userInput)
        ct += 1
    else:
        print("The number is already in the list!")
else:
    print("The numbers are:", userList)

