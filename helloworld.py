# A simple program that will print hello world and today's date and time
# This program was created by Wasay Khan on June 15th, 2020.

import datetime

print("Hello World!")

now = datetime.datetime.now()

print (now.strftime("Today is: %m-%d-%Y %H:%M:%S"))

print("This program was written by Wasay Khan on June 15, 2020")
