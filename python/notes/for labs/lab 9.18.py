first_list = input("Enter the first set of integer values separated by space: ").split()
second_list = input("Enter the second set of integer values separated by space: ").split()

print("Checking if the two lists are the same: ")

if first_list == second_list:
    print("Yes, they are.")
else:
    print("They are not.")

print("Checking if the two lists contain the same elements: ")

first_list.sort()
second_list.sort()

if first_list == second_list:
    print("Yes, they are.")
else:
    print("They are not.")
