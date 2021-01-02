"""
LISTS:
#lists use brackets
list_a = ['Joe', 7.26, 2.65, 'water'] # a list can contain mixed data types
list_b = ['Joe', [3.0, 2.4, 5.5], 100] # a list can contain lists inside of lists
list_a = list_a.append[1] # you can add things to lists
# tuples are also immutable

DICTIONARY:
# a comma separated list of 'Key : Value ' pairs enclosed by curly braces { }
sample_dictionary = {'favorite color' : 'blue', 'shoe size': 12}
print(sample_dictionary['favorite color'])
sample_dicitonary['ocean'] = 'blue' # how to add to a dictionary
sample_dicitonary['earth'] = 2      # also adding to a dictionary, can also use variables if needed

MIXING TYPES:
# if you mix integer and floating-point values in an arithmetic expression, the result is a floating point value
# you cannot add a string and an integer/float, but you can multiply strings by integers

FLOATING-POINT == INTEGER CONVERSION:
# you can convert integer to float and float to integer
int()
float()

BUILT IN MATHEMATICAL FUNCTIONS:
abs(x) # absolute value
round(x) # rounds to whole number
round(x , n) #rounds to a whole number and n decimal places
max(x, x1 , x2) # the largest value from among the arguments
min(x, x1 , x2) # the smallest value from among the arguments

MORE ABOUT STRINGS:
# they are a sequence of characters using quotations
# recommended to use "double quotations" because it will be easier getting used to it for JAVA
print("this is a string", "so is this")

STRING ESCAPE SEQUENCE:
\n # means new line
\\ # have to put two backslashes in strings if want it to look like \

CONCATENATION:
name = (firstName + lastName) # plus sign is concatenation, doesn't add space

STRING INDEXES:
str[last_character] == str[-1] == str[len(str)-1] # is accessing the last character, -1 == last character, 0 == first character
#strings are immutable - strings aren't able to be changed, must assign a new variable to the string if you want changed
a[2 : 6] # a[start : end], remember that have to put +1 for the end
a[ : : ] # beginning to end of the string
a[ : : -1 ] # reads everything backwards

a_str = 'abcdefyyuiop'
print(a_str[len(a_str)-1]) # returns the last character in the string
"""



