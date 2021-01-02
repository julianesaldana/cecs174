def updateList(ulist, ustr):
    j = 1
    for i in range(3):
        ulist[j] = ustr
        j += 1
    return ulist

def main():
    print("This program requires a list with a minimum of 4 items.")
    num = 0
    input_list = []
    while True:
        userInput = input("Enter the item of the list, or 'Q' to quit:")
        if userInput == "Q" or userInput == 'q':
            break
        else:
            input_list.append(userInput)
    if len(input_list) < 4:
        print("Not enough items in the list - goodbye.")
    else:
        input_str = input("Enter a string:")
        print(updateList(input_list, input_str))


main()









