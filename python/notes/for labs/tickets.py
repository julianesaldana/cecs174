tickets = 20
buyers = 0
print("There are currently %d tickets remaining." % tickets)
while 0 < tickets <= 20:
    user_input = int(input("How many tickets would you like to purchase?"))
    while (4 >= user_input > 0) and (user_input <= tickets):
        if (4 >= user_input > 0) and (user_input == tickets):
            tickets -= user_input
            buyers += 1
            break
        else:
            tickets -= user_input
            buyers += 1
            print("There are currently %d tickets remaining." % tickets)
            break
    else:
        print("Sorry, you can't buy that many.")

print("The total number of buyers was %d" % buyers)
