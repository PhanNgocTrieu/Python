
import math

def isPrime(number):
    max = math.ceil(number / 2)
    for num in range(2,max):
        if (number % num == 0):
            return False
    return True

_number = int(input("Give a number: "))

if (isPrime(_number) == True):
    print("It is a prime number")
else:
    print("It is not a prime number")