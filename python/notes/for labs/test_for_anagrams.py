def testForAnagram(first, second):
    if len(first) == len(second):
        return "Different words"
    else:
        counter = 0
        for i in range(len(first)):
            for j in range(len(second)):
                if first[i] == second[j]:
                    counter += 1
                    break
        if counter == len(first):
            return "Anagram"
        else:
            return "Different words"

