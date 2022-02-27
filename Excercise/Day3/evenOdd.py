#   problems:
#       Input: _number ->  Output: even/odd
#       Checking whether the input number is even or odd

_number = int(input("What is the number? : "))
if _number % 2 == 0:
    print(f"{_number} is even number")
else:
    print(f"{_number} is odd number")