#defines a function
def Hello():
    print("This is my first Python Function!")

#accesses the function
Hello()

def Hello2(Greeting):
    print(Greeting)

Hello2("This is an interesting function.")

Hello2("Another message...")

Hello2(1234)

Hello2(5+5)

def AddIt(Value1, Value2):
    print(Value1, "+", Value2, "=", (Value1 + Value2))

AddIt(2, 3)

AddIt(Value2 = 3, Value1 = 2)

def Hello3(Greeting = "No Value Supplied"):
    print(Greeting)

#prints the string provided
Hello3()

Hello3("This is a string.")

Hello3(5)

Hello3(2 + 7)

#used to print a variable number of elements
def Hello4(ArgCount, *VarArgs):
    print("You passed ", ArgCount, " arguments.")
    for Arg in VarArgs:
        print(Arg)

Hello4(1, "A Test String.")

Hello4(3, "One", "Two", "Three")

def DoAdd(Value1, Value2):
    return Value1 + Value2

print("the sum of 3 + 4 is ", DoAdd(3,4))

print("3 + 4 equals 2 + 5 is ", (DoAdd(3,4)==DoAdd(2,5)))

#The input is made into a variable
Name = input("Tell me your name: ")
print("Hello ", Name)

ANumber = float(input("Type a number: "))
print("You typed: ", ANumber)