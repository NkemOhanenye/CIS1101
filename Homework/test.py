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