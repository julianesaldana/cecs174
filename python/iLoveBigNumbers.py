input1 = input("Enter a number  ")
factorial = 1
for i in range(1, int(input1) + 1):
    factorial *= i
print(factorial)

factorial_sum = 0
factorial_string = str(factorial)
for i in range(factorial):
    factorial_sum += int(factorial[i])
print(factorial_sum)
