#  display the output (the number of characters, words, and lines in that files.)
file_name = input("Enter the input file name:")
infile = open(file_name, "r")
contents = infile.read()
contents2 = contents.rstrip().split()
infile.close()

characters = len(contents)
lines = 0
words = len(contents2)

for i in contents:
    if i == "\n":
        lines += 1
#actual words
#words = 0
#for element in contents2:
#    if element.isalpha():
#        words += 1

print("The file contains %d characters, %d words and %d lines"% (characters, words, lines))

