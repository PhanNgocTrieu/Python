print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

_leftOrRight = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')

if _leftOrRight.lower() == "left":
    _swimOrWait = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if _swimOrWait.lower() == "wait":
        _openDoor = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. wich colour do you choose?\n")
        if _openDoor.lower() == "yellow":
            print("Found the treasure, You Win!")
        elif _openDoor.lower() == "red" or _openDoor.lower() == "blue":
            print("You get attacked by an angry trout, Game Over")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif _swimOrWait.lower() == "swim":
        print("You are eaten by crocodile, Game Over!")
    else:
        print("Error of typing!")
elif _leftOrRight.lower() == "right":
    print("You fell into a hole, Game Over!")
else:
    print("Error of typing!")
