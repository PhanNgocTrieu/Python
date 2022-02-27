# Exercise:
#       Problems: Enter two digits numbers -> print the result for sum of two digits
#
#       Upgrade problems: just receiving 2 digit numbers -- if more digit -> error
#

# Normal problems:
two_digit_number = input("Give me two digit numbers: ")
_FristDigit = two_digit_number[0]
_SecondDigit = two_digit_number[1]
result = int(_FristDigit) + int(_SecondDigit)
print("Result: ", result)


while True:
    __input = input("Give me two digit numbers: ")
    if len(__input) == 2:
        if (__input[0].isdigit() or __input[1].isdigit()):
            print("Result - sum of digits: ", int(__input[0]) + int(__input[1]))
            break
        else:
            print("<ERR>:The input is not the digit number!!")
    else :
        print("<ERR>:The length of input was not suitable!!!")