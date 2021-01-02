class multiple_gpa:
    def __init__(self):
        self.num_classes = 0
        self.grades = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

    def getGPA(self):
        while True:
            self.num_classes = int(input("How many classes are you taking? "))
