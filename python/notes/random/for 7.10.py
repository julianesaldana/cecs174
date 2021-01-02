def swap(values):
    values[0], values[-1] = values[-1], values[0]


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
