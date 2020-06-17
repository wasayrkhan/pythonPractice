# Wasay Khan
# This is my second Python project 
# This program was created on June 15th, 2020.


print("\n\n*****CALCULATIONS*****.\n\nIn this project, users will be asked to input two integers.\nThen the program will display the sum, difference and product of the two numbers.")

int1 = int(input("\nPlease enter the first integer: "))
int2 = int(input("Please enter the second integer: "))

addition = int1 + int2
difference = int1 - int2
product = int1 * int2

print("\nThe sum of the two integers is " + str(addition))
print("The difference between the two integers is " + str(difference))
print("The product of the two numbers is " + str(product))

if product%2 == 0 :
    print("The product of the two integers is even")
else :
    print("The product of the two integers is odd")

print()

