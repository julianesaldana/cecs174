'''
hour1, minute1 = input(), input()
print(hour1)
print(minute1)
'''

'''
NESTED LOOPS:
# when a loop is inside another loop
for ...:
    while ...:
        if ...:
        
for in range(1,6):
    for j in range (6,11):
        print(i, j)

while True:
    user = input("enter a positive number or -1 to quit")
    if user = -1:
        break
    while not user.isdigit():
    user = input("Invalid, enter again: ")
    
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()
    
ENUMERATE():
# retrieves pairs containing a count (starting from 0) and a corresponding value of a sequence.
#i.e. enumerate(seq.) returns: ((0, sequence[0]), (1, sequence[1]), etc...)
pet_list = ['Yogurt', 'Mango', 'Prince']

for index, name  in enumerate (pet_list):
    print(index, name)
            #or
for i in range (len(pet_list)):
print(i, pet_list[i])

LOOP ELSE:
a = 7, or 2
while a > 5:
    print("A is greater than 5"0
    a -= 1
    break
else:
    print("else block: no break")
print("after while")

#else still works in "for" and "while" functions
'''

