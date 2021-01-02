def pwValidation(pw):  #negative logic is usually shorter and cleaner
    if len(pw) < 8 or pw.isupper() or pw.islower() or pw.isdigit() or not pw.isalnum():
        return False
    else:
        return True


def main():
    ct = 0
    while ct < 3:
        first_pw = input("enter a password: ")
        if pwValidation(first_pw):
            second_pw = input("second attempt of the pw: ")
            if first_pw == second_pw:
                print("matching")
                break
            else:
                print("not matching")
        else:
            print("your password does not meet complexity requirements!")
        ct += 1
    else:
        print("You have not provided a valid password!")


main()
