class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


person1 = BankAccount(2250)
while True:
    user_choice = input("What would you like to do?\n\tWithdraw\n\tDeposit\n\tQuit\n").lower()
    if user_choice == "withdraw":
        person1.withdraw(int(input("How much would you like to withdraw? ")))
    if user_choice == "deposit":
        person1.deposit(int(input("How much would you like to deposit? ")))
    if user_choice == "quit":
        print("Your balance is {}".format(person1.balance))
        break
