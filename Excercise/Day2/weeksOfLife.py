# source: https://waitbutwhy.com/2014/05/life-weeks.html
# problems: weeks of life
#   input: current year
#   output: "You have {days} days, {weeks} weeks, {years} years to live"

age = int(input("Enter your current age: "))

_yearsRemaining = 90 - age
_daysRemaining = _yearsRemaining * 365
_weeksRemaining = _yearsRemaining * 52
_monthRemaining = _yearsRemaining * 12

print(f"You have {_daysRemaining} days, {_weeksRemaining} weeks, {_monthRemaining} years to life")

