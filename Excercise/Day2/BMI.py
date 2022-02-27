# BMI - Body mass index
# BMI is derived from the mass (weight) and height of a person
# BMI is define as the body mass divided by the square of the body height
# -> Calculating BMI of a person

_weight = int(input("Enter your mass (weight - kg): "))
_height = float(input("Enter your height (m): "))

_BMI = _weight / (_height**2)

print("Your BMI: ", _BMI)


