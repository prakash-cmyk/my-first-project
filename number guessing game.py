
#Random Number Guesser

import random

print("welcome to the Random Number Guesser.!")

x=int(input("please enter the first value "))
y=int(input("please enter the second value"))

random_number=random.randint(x,y)

guess=None            #x<=N<=y
attempts=0  #attempts the user has made
guessed= False

while(not guessed):
    guess=input("please enter a guess between x and y")
    if guess.isdigit():
        guess=int(guess)

        if guess>random_number:
            print("guess is too high.!")
        elif guess<random_number:
            print("guess is too low.!")
        else:
            guessed=True

        attempts+=1
    else:
         print("invalid input , please try again.")

# while loop stopped running
print("you guessed it!\n it took you",attempts,"attemps to guess ", random_number)


