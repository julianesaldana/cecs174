def sumOfPattern(m, n):
    total_sum = 0
    m_string = ""
    for i in range(n):
        m_string += str(m)
        total_sum = total_sum + int(m_string)
    return total_sum

if __name__ == '__main__':
   print(sumOfPattern(int(input("Enter a first number")), int(input("Enter a second number"))))