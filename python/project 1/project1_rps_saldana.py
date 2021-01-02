# project1_rps_saldana.py
#
# Name: Julian Saldana
#
# Date: September 29, 2019
#
#

import random

user = input("Enter a move that is either rock, paper, or scissors: ").lower()    #doesn't matter if user input is capitalized or lowercase
while user != "rock" and user != "paper" and user != "scissors":                 #input validation, loop will activate if user enters incorrect input
    print("You must enter either rock, paper, or scissors!")
    user = input()                                                                #asks for input again
    if user == 'rock' or user == 'paper' or user == 'scissors':
            break                                                                 #loop will break until user enters a proper input
while user == 'rock' or user == 'paper' or user == 'scissors':
    comp = random.choice(['rock', 'paper', 'scissors'])                           #list that comp will use
    print("You chose:", user)
    print("Computer chose:", comp)
    if user == comp:                                                              #checks first if both user and comp inputs are equal, if so, it is a tie
        print("It's a tie")
    elif user == 'rock':                                                          #checks if user entered rock, compares it to comp is scissors, then determines who wins
        if comp == 'scissors':
            print("You won!")
        else:
            print("You lost!")
    elif user == 'paper':                                                         #checks if user entered paper, compares it to comp is rock, then determines who wins
        if comp == 'rock':
            print("You won!")
        else:
            print("You lost!")
    elif user == 'scissors':                                                      #checks if user entered scissors, compares it to comp is rock, then determines who wins
        if comp == 'paper':
            print("You won!")
        else:
            print("You lost!")
    play_again = input("Would you like to play again? Enter \"yes\" if so: ").lower()       #asks the user if they would like to play again
    if play_again == "yes":
        print("Enter a move that is either rock, paper, or scissors.")                      #if yes, user enters move again
        user = input().lower()
        if user == "rock" or user == "paper" or user == "scissors":                         #input validation
            continue
        else:
            while user != "rock" or user != "paper" or user != "scissors":                  #if user does not enter correct input, loop will continue until they do so
                print("You must enter either rock, paper, or scissors!")
                user = input()
                if user == 'rock' or user == 'paper' or user == 'scissors':
                    break                                                                   #if user enters a correct input, the loop will break to the original while loop
    else:
        print("Thanks for playing!")                                                        #if user types anything other than yes when asked to keep playing,
        break                                                                               # the original while loop breaks
