input_string = input("Enter your string here: ")
while input_string[-1] == "$":
    input_string.find("$"[::-1])
    input_string
    input_string = input_string.replace(input_string[-1], "")
print(input_string)
