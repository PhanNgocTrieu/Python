# if we do this below -> getting error
# because this below is integer -> integer has no len() function
# print(len(1234))

# Data Types:

# String:
# we always start with 0 because we with with binary -> binary start from 0
from re import T


print("Hello"[0]) # --> output: H

# This one wouble be error because 5 is out range!
# from H to o in string: we count from 0 -> 4
# so if you want to take 'o' -> replace it for 4 as below
# print("Hello"[5]) --> error
print("Hello"[4])



# the different of string and integer in print
print("1234" + "5678") #output: 12345678 Type of this is string
print(123 + 345) #output: 468 --> Type of this is integer

# float type
_floatVar = 3.1424213231
# print("float number " + _floatVar) # ---> error because we could not concatenate the string with float number
print("float number: ", _floatVar) # ---> We can print by this way

# Boolean
_isTrue = True
_isFalse = False

print("True variable: ", _isTrue)
print("False variable: ", _isFalse)
