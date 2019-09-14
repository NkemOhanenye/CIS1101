from array import *

vals = array('i', [5,9,8,4,2])

newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)

values = array('u', ["a","s","f","r","t"])

for g in values:
    print(g)
"""
while k<len(newArr):
    print(newArr[k])
    k+=1
"""