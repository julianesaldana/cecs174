tryAgain = "yes"

while tryAgain == "yes":
    time1 = input("Enter the first time as hours:minutes in 24 hour format:")
    time2 = input("Enter the second time as hours:minutes in 24 hour format:")

    while ":" not in (time1 and time2):
        print("Invalid format!!!")
        time1 = input("Enter the first time as hours:minutes in 24 hour format:")
        time2 = input("Enter the second time as hours:minutes in 24 hour format:")

    while not ((time1.replace(':', '').isnumeric()) and (time2.replace(':', '').isnumeric())):
        print("Invalid entry - input should be numbers only.")
        time1 = input("Enter the first time as hours:minutes in 24 hour format:")
        time2 = input("Enter the second time as hours:minutes in 24 hour format:")

    hour1 = int(time1.split(":")[0])
    min1 = int(time1.split(":")[1])
    hour2 = int(time2.split(":")[0])
    min2 = int(time2.split(":")[1])

    while not ((0 <= hour1 < 23) and (0 <= hour2 < 23) and (0 <= min1 < 60) and (0 <= min2 < 60) and (len(time1) <= 5) and (len(time2) <= 5)):
        print("Invalid time range.")
        time1 = input("Enter the first time as hours:minutes in 24 hour format:")
        time2 = input("Enter the second time as hours:minutes in 24 hour format:")

        hour1 = int(time1.split(":")[0])
        min1 = int(time1.split(":")[1])
        hour2 = int(time2.split(":")[0])
        min2 = int(time2.split(":")[1])

    hour1 = int(time1.split(":")[0])
    min1 = int(time1.split(":")[1])
    hour2 = int(time2.split(":")[0])
    min2 = int(time2.split(":")[1])

    while (0 <= hour1 < 23) and (0 <= hour2 < 23) and (0 <= min1 < 60) and (0 <= min2 < 60) and (len(time1) <= 5) and (len(time2) <= 5):
        if hour1 < hour2:
            print("time1 comes first")
        elif hour1 == hour2:
            if min1 < min2:
                print("time1 comes first")
            elif min1 == min2:
                print("time1 and time2 are the same")
            else:
                print("time2 comes first")
        else:
            print("time2 comes first")
        break

    tryAgain = input("Would you like to try again, 'Yes' for continue, quit otherwise:").lower()

    if tryAgain == "yes":
        continue
    else:
        print("Goodbye")
        break
