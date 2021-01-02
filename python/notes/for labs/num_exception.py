summation = 0
while True:
    try:
        num = float(input("Enter a number, or 2 non-numbers to quit:"))
        summation += num
    except ValueError:
        try:
            num = float(input("Enter a number, or another non-number to quit:"))
            summation += num
        except ValueError:
            print("The total is", format(summation, ".1f"))
            break
