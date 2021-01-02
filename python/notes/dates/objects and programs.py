"""
OBJECTS AND PROGRAMS / OOP:
# programming style in which tasks are solved by collaborating objects:
    - each object has its own set of data, together with a set of methods that act upon the data
# Object oriented programming (OOP):
    - the data and the functions are encapsulated into an entity called "class"
    - variable ares called attributes
    - functions are called methods
    - a class can be thought of as a BLUEPRINT, or a specification of object
    - class describes objects with the same behavior
    - object is a specific instance of a class
    - instance is a manifestation of a class
        # class = house
            # instance of house = 2 story house
        # class = car
            # instance of car = 4 door
# why use?
    - easier to understand OOP code in case of large, complex, projects
# key concepts:
    - public interface = the set of all methods provided by a class, together with a description of their behavior
    - to use a class, all you need to know is the public interface
    - encapsulation = the process of providing a public interface, while hiding the implementation details
        # restricting access to certain attributes and methods
    - inheritance = the ability to have one class inherit methods from another class
    - polymorphism = refers to a programming language's ability to process objects differently depending on their data type or class
        # the same method can be called on different data type
            - ex. function Add(x, t: Integer): Integer;
                  function Add(s, t: String): String
# defining a class and an instance:
    - "class" is used
        # ex:
            class BankAccount(object)/BankAccount:
    - creating an instance is the manifestation(version) of the class
        # ex:
            myAccount = BankAccount()
    - calling the print() on a class return its type
        # returns the location of the class and the type
# when calling a functoin, the number of arguments needed to match to its definition, however this is not the case with a class method
# instance will pass in as 1st argument when calling method in a class
    - this value gets assigned to the variable called "self"
# polymorphism
    - refers to a programming language's ability to process objects differently depending on their data type or class
    - example:
        for obj in garage:
            obj.move()
    - not polymorphism
       for obj in garage:
            if instance(obj, bike):
                obj.move()
            if instance(obj, car):
                obj.move()
# checking type
    - isinstance()
        print(isinstance(my_bike, Car))
    - issubclass()
# special method - magic/dunder
    def __repr__(self):
        statement
    def __str__(self):
        statement
    my_car = Car("blue", "35 mph")
    print(my_car) # returns a string, without __str__ / __repr__, it will print hexadecmial location

    - isequal(), mulitiply, etc
        def __eq__(self #leftvalue, rightValue):
            your code for compare operation
        if inst_1 == inst_2: # calls myClass.__eq__(inst_1, inst_2)
            statement
        # ex:
            print(3==4) # really means print(int.__eq(3,4))

"""
