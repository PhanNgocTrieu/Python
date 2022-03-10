import rano_dom

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# _user = int(input("Choose 0 - Rock, 1 - Paper or 2 - Scissor? "))

game_images = [rock, paper, scissors]
_useChoice = int(input("Choose 0 - Rock, 1 - Paper or 2 - Scissor? "))
_bot = rano_dom.randint(0,2)

print(game_images[_useChoice])
print("Computer choice:")
print(game_images[_bot])


if _useChoice == 0 and _bot == 2:
    print("You Win!")
elif _bot == 0 and _useChoice == 2:
    print("You Lose!")
elif _bot > _useChoice:
    print("You Lose!")
elif _useChoice > _bot:
    print("You Win")
elif _bot == _useChoice:
    print("It's a draw")
else:
    print("You typed an invalid number, you lose!")