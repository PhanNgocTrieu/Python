
for elems in range(0, 101):
    if (elems % 3 == 0 and elems % 5 == 0):
        print("Fizz Buzz")
    elif (elems % 3 == 0):
        print("Fizz")
    elif (elems % 5 == 0):
        print("Buzz")
    else:
        print(elems)

