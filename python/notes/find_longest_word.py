def findLongestWord(a_str):
    wordlist = a_str.split()
    wordmax = wordlist[0]
    for i in range(len(wordlist)):
        if len(wordlist[i]) >= len(wordmax):
            wordmax = wordlist[i]
    return wordmax

if __name__ == '__main__': ## for your own module test
    print(findLongestWord(input("Enter a sentence: ")))

