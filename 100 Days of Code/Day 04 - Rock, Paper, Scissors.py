import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
game = [rock, paper, scissors]
print(game[player])

computer = random.randint(0,2)
print("Computer chose: ")
print(game[computer])

if player == 0:
    if computer == 0:
        print("It's a draw!")
    elif computer == 1:
        print("You lose!")
    else:
        print("You win!")
elif player == 1:
    if computer == 0:
        print("You win!")
    elif computer == 1:
        print("It's a draw!")
    else:
        print("You lose!")
elif player == 2:
    if computer == 0:
        print("You lose!")
    elif computer == 1:
        print("You win!")
    else:
        print("It's a draw!")
else:
    print("You chose an invalid number, you lose!")