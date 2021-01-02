def main():
    attempts = 0
    while attempts < 3:
        user = input("Enter a new password: ")
        if validatePassword(user) is False:
            print("your password does not meet complexity requirements")
            attempts += 1
            continue
        else:
            validation = input("Please re-enter the same password: ")
            if validation == user:
                print("Password is valid and two entries are matching")
                break
            else:
                print("Passwords do not match!")
                attempts += 1
                continue
    else:
        print("You have not provided a valid password, goodbye!")


def validatePassword(password):
    if len(password) < 8 or not password.isalnum():
        return False
    lower = 0
    upper = 0
    digit = 0
    for i in range(len(password)):
        if password[i].islower():
            lower = 1
        if password[i].isupper():
            upper = 1
        if password[i].isdigit():
            digit = 1
    if lower == 1 and upper == 1 and digit == 1:
        return True
    else:
        return False



main()