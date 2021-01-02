def reverseString(a_str):
    a_str = a_str.split(" ")
    print(a_str)
    for i in range(0, len(a_str), 2):
        a_str[i] = a_str[i][::-1]
    a_str = " ".join(a_str)
    return a_str




if __name__ == '__main__': ## for your module test
    print(reverseString(input("Enter a sentence: ")))
