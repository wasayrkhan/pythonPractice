# Wasay Khan
# This is my third Python project 
# This program was created on June 16th, 2020.

# Importing "random" for the randint function
import random

# guessesTaken is to keep track of how many guesses the user has already made. The user is allowed a total of 3 guesses 

guessesTaken = 0

print("Hello! Welcome to Guess the Number!")

name = input("Please enter your name: ")
print("Get ready " + name, "! Let's play Guess the Number")

# Assigning a random integer to the variable "number" using 
number = random.randint(1,20)

print("Pick a number between 1 and 20: ")

while guessesTaken < 6 :
    print("Take a guess:")
    guess = int(input())

    guessesTaken = guessesTaken + 1 

    if guess < number :
        print("The number you guessed is too low")

    elif guess > number :
        print("The number you guessed is too high")

    else :
        print("The two numbers are equal")

    break

if guess == number :
    guessesTaken = str(guessesTaken)
    print("Good job! You guessed the number in " + guessesTaken + " guesses!")

elif guess != number:
    number = str(number)
    print("You were incorrect! The number I was thinking was " + number)