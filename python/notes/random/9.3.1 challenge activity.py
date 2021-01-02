"""
num_guesses = int(input())
user_guesses = []

length = len(str(num_guesses))
for num in range(length):
    user_guesses.append(num_guesses[num])

print('user_guesses:', user_guesses)
"""

"""
user_input = input()
test_grades = list(map(int, user_input.split())) # contains test scores

sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0
for num in test_grades:
    if num > 100:
        sum_extra += (num - 100)


print('Sum extra:', sum_extra)
"""

user_input = input()
hourly_temperature = user_input.split()

for temp in hourly_temperature:
    if temp == hourly_temperature[-1]:
        print(temp, end=' \n')
    else:
        print(temp, '->', end=' ')
