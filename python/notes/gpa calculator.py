numClasses = int(input("Enter the number of classes you are taking: "))
grades = {"a": 4, "b": 3, "c": 2, "d": 1, "f": 0}
overallGrade = 0
grade = 0
for i in range(numClasses):
    grade = input("Enter the letter grade: ").lower()
    overallGrade += grades[grade]
gpa = overallGrade / numClasses
print(gpa)
