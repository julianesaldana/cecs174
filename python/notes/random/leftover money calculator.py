class Account:
    def __init__(self, total):
        self.total = total
        self.spent = 0

    def calculator(self):
        while True:
            amount = int(input("What have you spent so far? or type any negative number to quit: "))
            if amount > 0:
                self.total -= amount
                self.spent += amount
            else:
                return "Your left over money = {}\nThe amount you've spent = {}".format(self.total, self.spent)



loan_amount = Account(int(input("How much do you have to spend?")))
print(loan_amount.calculator())

