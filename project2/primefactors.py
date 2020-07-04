# This program was created by Wasay Khan on June 21st, 2020. 
# A program designed to take user input 2 times (the integer and the selection) and then list either prime factors leading up to that integer or it will factorize the integer 

import math
import sys

# Defining a function that will ask the user what they want to do
def choice(): 
    print("\nPlease select and option from the following choices: \n1. List all prime factors.\n2. Factorize the integer.\n0. Exit")
    selection = int(input())
    return selection


num = int(input("Please enter a number between 1 and 99: "))

# While loop asking user for the integer they want to either factorize or find prime numbers leading up to..
while ((num < 0) or (num > 100)):
    print("Error! The number you entered is not within the specified range!")
    num = int(input("Please enter a number between 1 and 99: "))
    continue

choice = choice()

# Using a while loop to see what the user enters as their "choice". If statements are used since "switch/case" is not allowed in python. 

while choice != 0:

    print("\nPlease select and option from the following choices: \n1. List all prime factors.\n2. Factorize the integer.\n0. Exit")
    choice = int(input())
    
    if choice == 1:
        for x in range(1, num):
            if x > 1:
                for i in range(2, num):
                    if (x % i) == 0:
                        break
                else:
                    print(x)

    if choice == 2:
        print("Factors of %d \n", num)
        for factor in range (1, num):
            if factor%num == 0:
                print(factor)
                continue

    if choice == 0:
        sys.exit()
        break