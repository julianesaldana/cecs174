class Employee:
    num_of_emps = 0
    raise_amount = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "The first name is {}".format(self.first)

    def __str__(self):
        return "The last name is {}".format(self.last)

    def apply_raise(self):
        self.pay *= Employee.raise_amount


emp1 = Employee("Tom", "Selleck", 5000)
emp1.apply_raise()
print(emp1.pay)
emp2 = Employee("Sam", "Black", 3000)
print(emp2.pay)

print(emp1)