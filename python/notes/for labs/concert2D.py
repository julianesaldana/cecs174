price_chart = [[10, 10, 10, 10, 10],
               [20, 20, 20, 10, 10],
               [20, 20, 20, 10, 10],
               [20, 20, 20, 10, 10],
               [40, 30, 30, 20, 20]]
user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:").lower()
while user_input != "s" and user_input != "p" and user_input != "q":
    print("That wasn't a valid option.")
    user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:").lower()
while user_input == "s" or user_input or "p" or user_input == "q":
    if user_input == "s":
        row = int(input("Enter the row: "))
        column = int(input("Enter the column: "))
        price = price_chart[row - 1][column - 1]
        if price != 0:
            print("Sold, for $%d!" % price)
            price_chart[row - 1][column - 1] = 0
        else:
            print("Sorry, that seat is not available.")
    if user_input == "p":
        price = int(input("How much do you want to spend?"))
        counter = 0
        for row in range(len(price_chart)):
            if price in price_chart[row]:
                counter = 1
                location = price_chart[row].index(price)
                print("You can have seat", row + 1, location + 1)
                price_chart[row][location] = 0
                break
        if counter == 0:
            print("Sorry, no tickets available at that price.")
    if user_input == "q":
        for row in price_chart:
            for column in row:
                print(column, end=" ")
            print()
        break
    user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:").lower()
    while user_input != "s" and user_input != "p" and user_input != "q":
        print("That wasn't a valid option.")
        user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:").lower()
