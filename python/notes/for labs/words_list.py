file_name = input("Enter the input file name:")

infile = open(file_name, "r")
user_file = infile.read().split()
infile.close()

in_common_words = open('100-most-common-words.txt', "r")
common_words = in_common_words.read().split()
in_common_words.close()

not_in_list = []
for word in user_file:
    if word not in common_words:
        not_in_list.append(word)

print("The following words are not in the 100 most common word list:")
for word in not_in_list:
    print(word)
