import random
comp = random.randint(1, 10)
correct = 0
numGuesses = 0

print("I am thinking of a number between 1 and 10.")

while correct == 0:
    while numGuesses < 5:
        guess = input("Take a guess:")
        while not guess.isdigit():
            guess = input("Wrong value, re-enter:")
        while guess.isdigit():
            while not 0 <= int(guess) <= 10:
                guess = input("Wrong value, re-enter:")
            numGuesses += 1
            guess = int(guess)
            if guess > comp:
                print("Too high")
            if guess < comp:
                print("Too low")
            if guess == comp:
                print("Good job, you got it with %d guesses" % numGuesses)
                numGuesses = 6
                correct = 1
            break
    while numGuesses == 5:
        print("You guessed wrong, the number I was thinking of was %d" % comp)
        correct = 1
        break
