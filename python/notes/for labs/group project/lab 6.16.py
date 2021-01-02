while True:
    menu_input = int(input(("******** menu ********\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - "
                            "Division\n5 - Exit\nPlease select the operation:")))
    if 1 <= menu_input <= 4:
        num_one = int(input("Enter the first number:"))
        num_two = int(input("Enter the second number:"))
        if menu_input == 1:
            sum = num_one + num_two
            print("The result is", sum)
        if menu_input == 2:
            sub = num_one - num_two
            print("The result is", sub)
        if menu_input == 3:
            mult = num_one * num_two
            print("The result is", mult)
        if menu_input == 4:
            div = num_one / num_two
            print("The result is", div)
        continue
    else:
        print("Goodbye")
        break
