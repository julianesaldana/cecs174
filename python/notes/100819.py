"""
PASSING PARAMETER ARGUMENT:
#parameter (variables) receive the argument(values) supplied in the function call
#the parameter is:
    like a variable definition
    declared in the function
    initialized with the value of the argument
#argument is:
    the value being passed in
#ex:
def addTwoNum(n1, n2):
    result = n1 + n2
    return result
addTwoNum(1, 2)
#tips:
    do not modify parameter variables
    introduce a separate variable

RETURN:
#is the output that a function computes
#returns once value or none
#if it returns more than one value, it is a list, tuple, or dictionary

MULTIPLE RETURN:
#a function can use multiple reutrn statements, every branch must have a return statement
def cubeVolume(sidelength):
    if sidelength < 0:
        return 0
    else:
        statements
        ...
        return result

MAKE SURE RETURN CATCHES ALL CASES:
#missing return statement:
    make sure all conditions are handled

def cubeVolume(sideLength):
    if sideLength >= 0:
        return sideLength ** 3
    # LOGIC error - no return value if sideLength < 0, nothing will happen
"""
