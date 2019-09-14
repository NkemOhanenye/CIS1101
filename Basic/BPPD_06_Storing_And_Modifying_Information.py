myVar = 5
print(myVar)

print(bin(myVar)) #binary: 00000101
print(oct(myVar)) #base 8
print(hex(myVar)) #hexadecimal: 05

Test = 255.0
print("Direct Assignment: ", Test)

Text = 2.55e2
print("Scientific Notation: ", Test)

Test = 2.55e-2
print("Negative Exponent: ", Test)

myComplex = 3 + 4j
print(myComplex.real) #real number
print(myComplex.imag) #imaginary number

myBool = 1 > 2
print(myBool)

print(ord("A")) #Displays letter to numeric equivalent

myInt = int("123")
print(myInt) #parses string to int

print(type(myInt)) #Displays the type of variable

myStr = str(1234.56)
print(myStr) #parses int to string
print(type(myStr))

#prints the time detailed
import datetime
print(datetime.datetime.now())

#prints the date
print(str(datetime.datetime.now().date()))

