row1 = ["😒","😒","😒"]
row2 = ["😂","😂","😂"]
row3 = ["🌳", "🏝","🌳"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where you do want to put the treasure? (11->33): ")

_xPos = int(position[0])
_yPos = int(position[1])

map[_xPos - 1][_yPos - 1] = 'X'

# print(map[_yPos - 1])

print(f"{row1}\n{row2}\n{row3}")
