'''
LISTS:
# is a container of that stores a collection of elements (items)
# data types can be mixed within a list
# a list can be one or more lists
# use [] to create a list
    to access - list()
    to access specific elements - list[]
# slices of a list
    to access - list[3:6]
    assign values to slice - list[3:6] = 1,2,3
# list is mutable while strings are immutable
    can append to the end of a list - list.append()
    can extend a list with other things after - list.extend(another_list)
# finding an element in list
    if element in list:
        statement
# finding element position:
    position = list.index(element)
# removing element:
    list.pop(element)
    # if you use pop without a parameter, it removes the last element in the list
# sorting a list from least to greatest
    list.sort() # only for lists, doesn't do anything but sorts, doesn't return
    sorted(list) # built in, used on strings and lists, and returns the sorted item
# max/min/sum
    max(list)
    min(list)
    sum(list)
# concatenation
    newlist = list1 + list2
    # similar to extend
# list references/memory
    #variables - reference to the list
    #contents - memory where the values are stored
    #a list variable contains a reference to the list contents(values)
    # the reference is the location of the list contents(in memory)
    # id() function
    # if you change the value of something in a list after statements, it
      changes it for the rest of the code, even before
# copy
    newlist = list.copy()
# comparing lists
    if list1 == list2:
        statement etc
# list nesting
    list = [1,2,3, anotherlist, 4]
# to see elements of a 2D list:
    for row in my_list:
        for column in row:
            print(column, end =' ')
        print()
# list = [expression for name in iterable]
    my_list = [50, 23, -4]
    my_list_minus10 = [(element - 10) for element in my_list]
    #this means that a list has an embedded for loop

'''