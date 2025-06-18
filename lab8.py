# while loops

import random

print("Welcome to the Guess the Number!")
print("The rules are simple. I will think of a number and you wil try to guess it.")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again!".format(guess))