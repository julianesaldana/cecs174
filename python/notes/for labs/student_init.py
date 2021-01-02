class Student:
    num_students = 0

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.quiz_num = 0
        Student.num_students += 1

    def getName(self):
        return self.name

    def addQuiz(self, score):  # calling the class attribute
        self.score += score
        self.quiz_num += 1

    def getTotalScore(self):
        return self.score

    def getAverageScore(self):
        return self.score / self.quiz_num

    def totalStudents(self):
        return self.num_students


st1 = Student('Jim Black')
print(st1.getName())
st1.addQuiz(10)
st1.addQuiz(20)
print(st1.getTotalScore())
print(st1.getAverageScore())

st2 = Student('Jack Brown')
print(st2.getName())
st2.addQuiz(10)
st2.addQuiz(20)
st2.addQuiz(30)
print(st2.getTotalScore())
print(st2.getAverageScore())

print(Student.num_students)

