"""
EXCEPTIONS:
# errors that are detected during the execution of the program.
# this can be done using the "try" and "except"
# "try" block contains one or more statements that may cause an exception
# each "except" clause contains the handler for an exception type

try:
    statements
except exception_1:
    statements
except exception_2:
    statements
except:
    statements

# example:
    try:
        x = int(input())
        y = int(input())
        print("The result is", x/y)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Need to enter a number.")
    ## except can combine like:
    except(ZeroDivisionError, ValueError, TypeError,..etc.):
        statements

# else and finally statements
    try:
        statements
    except:
        statements
    else: (optional, only happens if except hasn't occurred)
        statements
    finally: (optional, always executed regardless if put in)
        statements

# raise exception
    def area(l,w)
        if l <= 0:
            raise ValueError("Length must be a positive integer")
        if w <= 0:
            raise ValueError("Length must be a positive integer")
    def test():
        l = int(input())
        w = int(input())
        print("Area is, area(l, w))
    def main():
        try:
            test()
        except ValueError as e:
            print("Value Error:"", e)

except Exception as reason:
    print("Here is why:", reason)
"""