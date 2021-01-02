import random

random_list = []
for i in range(10):
    random_list.append(random.randint(0, 99))

print("Every other element of the random list (keep the first element):", end="")
for i in range(0, 10, 2):
    print(random_list[i], end=" ")

print()
print("The value of elements that are even:", end=" ")
for num in random_list:
    if num % 2 == 0:
        print(num, end=" ")

print()
print("Elements in reverse order:", end="")
for i in range(9, -1, -1):
    print(random_list[i], end=" ")

print()
random_list.sort()
print("Elements sorted:", end="")
for num in random_list:
    print(num, end=" ")
