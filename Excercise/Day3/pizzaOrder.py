print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L? ")
add_peperoni = input("Do you want pepperoni? Y or N. ")
extra_chees = input("DO you want extra cheese? Y or N.")

if size == "L":
    bill = 25
    if add_peperoni == "Y":
        bill += 3
if size == "M":
    bill = 20
    if add_peperoni == "Y":
        bill += 3
if size == "S":
    bill = 15
    if add_peperoni == "Y":
        bill += 2
if extra_chees == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")