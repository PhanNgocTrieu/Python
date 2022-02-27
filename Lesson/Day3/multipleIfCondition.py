print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket are $5")
    if age <= 18:
        bill = 7
        print("Youth ticket are $5")
    else:
        bill = 12
        print("Adult ticket are $12")

    isTakngPhoto = input("Do you want to a photo taken? Y or N. ")
    
    if isTakngPhoto == 'Y':
        # adding $3 to their build
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")