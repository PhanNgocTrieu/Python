# loop with lists

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print(fruits)


# using for loop with range function
numList = [1,2,3,4,5,6]

for num in range(0, len(numList)):
    print(f"idex: {num} - value: {numList[num]}")


total = 0
for elems in range(0, 100):
    total += elems
print("Total: ", total)

_sumOfEven = 0
for elems in range(2,101): # or for elems in rage (2,101,2):
    if (elems % 2 == 0):
        _sumOfEven += elems
print(f"Sum: {_sumOfEven}")
