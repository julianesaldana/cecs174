num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces
letter = "A"
for num in range(1, num_rows + 1):
    for num2 in range(1, num_cols + 1):
        print(str(num) + letter, end= " ")
        letter = chr(ord(letter) + 1)
    letter = "A"
print()