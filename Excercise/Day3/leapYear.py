# Problems:
#   Every year that is exactly divisible by four is a leap year, 
#   except for years that are exactly divisible by 100, but these centurial years are leap years 
#   if they are exactly divisible by 400
#
#   For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are
#
#
__year = int(input("Give the year:"))

if __year % 4 == 0:
    if __year % 100 == 0:
        if __year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")