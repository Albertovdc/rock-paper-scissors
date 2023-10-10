import random
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

game = [rock, paper, scissors]
option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
option_computer = random.randint(0,2)
if option >= 3:
    print("You losE, YOU INTRODUCE A INVALID NUMBER")

else:
    print(game[option])
    print("Computer choice:")
    print(game[option_computer])
    if option == 0 and option_computer == 2:
        print("You win")
    elif option == 2 and option_computer == 0:
        print("You lose")
    elif option_computer > option:
        print("You lose")
    elif option > option_computer:
        print("You win")
    elif option_computer == option:
        print("It's a draw")
