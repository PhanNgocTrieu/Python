print("Welcome to the tip calculator")
_totalBill = float(input("What was the total bill? $"))
_tipPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15? : "))
_numOfPeople = int(input("How many people to split the bill? : "))

_total = round((_totalBill + _totalBill * _tipPercentage / 100) / _numOfPeople,2)

print(f"Each person should pay: ${_total}")
