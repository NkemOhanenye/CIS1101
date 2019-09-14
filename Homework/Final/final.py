"""
    Author: Nkem Ohanenye
    Date: 12/12/18
    Purpose: Answer the questions to the final exam
"""

#Question 1
'the functions works on user input'
def ozToIG(value = input("Input a value for Oz to IG: ")):
    'calculates the inputed oz to imperial gallons'
    value = int(value) * 0.0065
    'rounds the number to 1 decimal point'
    value = round(value, 1)
    print(value)

ozToIG()

#Question 2
def ozToIG2(value = input("Input a value for Oz to IG: ")):
    "if the number is less than 0 then it won't be calculated"
    if int(value) > 0:
        value = int(value) * 0.0065
        value = round(value, 1)
        print(value)
    else:
        "the error message"
        print("Your entered number is too small")

ozToIG2()

#Question 3
'imports the random function'
import random

def loop():
    'used to count the times the number 3 appears'
    count = 0
    'prints the code within the loop 100 times'
    for x in range(100):
        'prints 0 - 10 in a random order'
        number = random.randint(0, 10)
        print(number)
        'checks to see if 3 appears'
        if number == 3:
            'increases count by 1 each loop'
            count += 1
    'outside of for loop to not print repeatedly'
    'the count number is divided by 100 then given a % for the percentage'
    print("\nThe number 3 appeared " + str((count/100)) + "% of the time.")

loop()

