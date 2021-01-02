"""
MEMBERSHIP OPERATORS:
if/while ' ' in ' '  #check to see if value is in the sequence
if/while ' ' not in ' ' #check to see if values is not in the sequence
!=  #not equal

STRING CONVERSION:
str()  #converting to string
int()  #converting to integer
float()  # converting to float

STRING OPERATIONS:
'a' + 'b' == 'ab'
70 + 70 == 140
70 + 70.0 == 140.0
'a' + 70 == error  # cannot add a string and integer together
last_in_string = string[len(string) - 1]

STRING METHODS:
s.lower()  #lowercase version of string s
s.upper()  #uppercase version of s
s.replace()  #a new version of string s in which every occurrence of the substring 'old' is replaced by the string 'new'
s.count()  #stores the number of times a string appears in the main string
s.split() #splits the string with given parameters
s.join()  #joins a list/string together
s.islower
s.isuper
s.isalpha
s.isalnum  #tests if these are what they say
ex: answer = input("enter 'yes' to continue otherwise quit.").lower()
    if answer == 'yes' .. etc


#work on lab ch.4 sec 10
NAMES = "January,  February March   April,  May      June     July     August   September October  November December        "

names_new = NAMES.split()

number = int(input("Enter a number between 1 and 12"))

if number>=1 and number<=12:
    print(number, 'is', names_new[number-1].strip(','))

else:
    print("ERROR")

#workd on lab ch.4 sec 13
sentence = input("Enter a sentence: \n")

if 'a' or 'i' or 'o' or 'u' in sentence:
    new_sentence = sentence.replace('a', 'e').replace('i','e').replace('o','e').replace('u','e')

if 'A' or 'I' or 'O' or 'U' in new_sentence:
    new_sentence = new_sentence.replace('A', 'E').replace('I','E').replace('O','E').replace('U','E')

print(new_sentence)

#work on lab ch.4 sec 12

word = input("Enter a string:")

if word[0] == word[-1]:
    print("Palindrome")
else:
    print("Different word")

#work on ch4 sec 14
word = input("enter a word")
while word[-1] == '$':
    word = ''.join(word.rsplit('$',1))
print(word)

"""

#work on ch4 sec 14
word = input("enter a word")
while word[-1] == '$':
    word = ''.join(word.rsplit('$',1))
print(word)