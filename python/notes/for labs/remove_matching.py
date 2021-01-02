original_list = input("Enter a string:").split()
print("Original list is", original_list)

final_list = []

for i in original_list:
    if len(i) < 4:
        continue
    else:
        final_list.append(i)

print("Final list is", final_list)



