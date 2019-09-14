import random

"""
    Author: Nkem Ohanenye
    Date: 11/19/18

    Purpose: Redo on old Problems:
    Chapter 1: problem 7
    Chapter 2: problem 5, 6
    Chapter 3: problem 5
    Chapter 4: problem 5
    Chapter 5: problem 3
"""

'Problem 1.7'
'the inputs of the tankSize, milesTraveled and gallonsLeft'
tankSize = float(input("Tank size?: "))
milesTraveled = float(input("How many miles have you traveled?: "))
gallonsLeft =float(input("How many gallons do you have left?: "))

'the calculation for miles per gallon'
mpg = milesTraveled/(tankSize - gallonsLeft)

"the 'mpg * tankSize' checks to see how many more miles you " \
"can go till you need to fill your tank"
fullTank = mpg * tankSize

'round is used to print only one decimal place'
print("You can drive", round(fullTank, 1),  "miles before you need to fill your tanks.")

'Problem 2.5'
'the user asks the user to enter 3 test scores'
print("Input three test scores: ")
score1 = float(input("Test 1: "))
score2 = float(input("Test 2: "))
score3 = float(input("Test 3: "))

'the average of the scores are taken'
average = (score1 + score2 + score3) / 3

'the following determines if the average was greater ' \
'than each number, to see what grade they recieved'
if average >= 90:
    print("You got an A!")
elif average >= 80:
    print("You got a B!")
elif average >= 70:
    print("You got a C.")
elif average >= 60:
    print("You got a D.")
else:
    print("You got an F.")

'Problem 2.6'
number = random.randint(1, 1001)
'a random number 1 - 1000 is picked then the following outputs the ending'
'if the mod of the number ends in 1, except 11, st'
if (number % 10 == 1) and (number % 100 != 11):
    print(str(number) + "st")
elif (number % 10 == 2) and (number % 100 != 12):
    'if the mod of number ends in 2, except 12, nd'
    print(str(number) + "nd")
elif (number % 10 == 3) and (number % 100 != 13):
    'if the mod of number ends in 3, except 13, rd'
    print(str(number) + "rd")
else:
    'the rest all end in th'
    print(str(number) + "th")

'Problem 3.5'
while True:
    'true in while is used to keep an eternal loop till exited'
    answer = input("Are you happy? (1 = yes, 2 = no): ")
    'if the answer is 1 or 2 the loop continues, else the loop asks you to try again'
    'to not return a variable mismatch (int and string) the answers are given in string' \
    'and compared in string'
    if (answer == "1") or (answer == "2"):
        if answer == "1":
            print("Good for you")
            "break is similar to 'exit loop' in visual logic"
            break
        else:
            print("I'm sorry to hear that")
            break
    else:
        print("Please try again.")

'Problem 4.5'
for lineCount in range(1, 10):
    'creates the first loop and a nested loop that loops the first loop'
    for triangle in range(lineCount):
        "the 'end=' is used to display the line horizontally instead of vertically"
        print(lineCount, end=" ")
    print("")

'Problem 5.3'
list = []
'creates a blank list and creates the count variable'
count = 0

'like in visual logic, the loops name is inputs and it loops between 1 and 10'
for inputs in range(1, 11):
    'a variable is used to recieve all the inputs, then all the inputs are appended to the list'
    data = int(input("input: "))
    list.append(data)
'the target number to count is asked'
targetValue = int(input("What is the target number?: "))
'the for loop target in the range of the length of the list.' \
'the length of the list stops the arry out of bounds error'
for target in range(len(list)):
    'the target length is looped to look at each number in the ' \
    'list to check if they are equal to the target value, if so, ' \
    'count increases'
    if targetValue == list[target]:
        count = count + 1
print("The value appears", count, "times in the array.")