time1 = input("Enter the first time as hours:minutes in 24 hour format:")
time2 = input("Enter the second time as hours:minutes in 24 hour format:")

if ':' in (time1 and time2):
    if time1.replace(':', '').isnumeric() and time2.replace(':', '').isnumeric():
        hour1 = int(time1.split(':')[0])
        hour2 = int(time2.split(':')[0])
        minute1 = int(time1.split(':')[1])
        minute2 = int(time2.split(':')[1])
        if (0 < (hour1 and hour2) < 24) and (0 < (minute1 and minute2) < 60) and len(time1) == 5 and len(time2) == 5:
            if hour1 < hour2:
                print("time1 comes first")
            elif hour1 == hour2:
                if minute1 < minute2:
                    print("time1 comes first")
                elif minute1 == minute2:
                    print("time1 and time2 are the same")
                else:
                    print("time2 comes first")
            else:
                print("time2 comes first")
        else:
            print("Invalid time range.")
    else:
        print("Invalid entry - input should be numbers only.")
else:
    print("Invalid format !!!")



