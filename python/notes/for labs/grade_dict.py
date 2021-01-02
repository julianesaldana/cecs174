students_grades = {}
students_grades_modified = {}

def gradeVerification(attempt):
    if len(attempt) != 0 or len(attempt) != 2:
        raise TypeError("Invalid grade, did not add record. Valid grades are 'A','B','C','D','F' !")
    elif not attempt[0].isalpha():
        raise TypeError("Invalid grade, did not add record. Valid grades are 'A','B','C','D','F' !")
    elif len(attempt) == 2 and (attempt[1] != "+" or attempt[1] != "-"):
        raise TypeError("Invalid grade, did not add record. Valid grades are 'A','B','C','D','F' !")
    else:
        return attempt


while True:
    options = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit?").upper()
    if options == "A":
        name = input("Enter the name of the student:")
        if name not in students_grades:
            grade = input("Enter the student's grade:")
            students_grades[name] = grade
        else:
            print("Sorry, that student is already present.")
    elif options == "R":
        name = input("What student do you want to remove?")
        if name not in students_grades:
            print("Sorry, that student doesn't exist and couldn't be removed.")
        else:
            students_grades.pop(name)
    elif options == "M":
        name = input("Enter the name of the student to modify:")
        if name not in students_grades:
            print("Sorry, that student doesn't exist and couldn't be modified.")
        else:
            print("The old grade is", students_grades.get(name))
            new_grade = input("Enter the new grade:")
            # students_grades[name] = new_grade
            students_grades.pop(name)
            students_grades_modified[name] = new_grade
    elif options == "P":
        if len(students_grades) != 0:
            students_grades.update(students_grades_modified)
            for name, grade in students_grades.items():
                print("%s %s" % (name, grade))
        else:
            print("No record found!")
    elif options == "Q":
        print("Goodbye!")
        break
    else:
        print("Sorry, that wasn't a valid choice.")
