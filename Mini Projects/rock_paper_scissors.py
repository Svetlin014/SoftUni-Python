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

user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:
    game_choices = [rock, paper, scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    if user_choice > 2 or user_choice < 0:
        print("Invalid number, please enter a number between 0 and 2 to proceed.")
        continue
    print(game_choices[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw for the round")
    elif user_choice == 0 and computer_choice == 1:
        print("You lost this round")
        computer_wins += 1
    elif user_choice == 0 and computer_choice == 2:
        print("You won this round")
        user_wins += 1
    elif user_choice == 1 and computer_choice == 2:
        print("You lost this round")
        computer_wins += 1
    elif user_choice == 1 and computer_choice == 0:
        print("You won this round")
        user_wins += 1
    elif user_choice == 2 and computer_choice == 0:
        print("You lost this round")
        computer_wins += 1
    elif user_choice == 2 and computer_choice == 1:
        print("You won this round")
        user_wins += 1

if computer_wins == 3:
    print(f'Computer wins {computer_wins}:{user_wins}')
else:
    print(f'User wins {user_wins}:{computer_wins}')
