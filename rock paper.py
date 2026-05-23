import random

choice = ['''
         _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)''','''
         _______
     ---'   ____)____
                ______)
                _______)
              _______)
      ---.__________) ''','''

          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___) '''
]
computer_choice = random.choice(choice)

choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
user_choice = choice[choice1]
print(computer_choice)
print("computer chose")
print(user_choice)
if user_choice == computer_choice:
    print("it's a Draw")
elif user_choice == choice[0] and computer_choice == choice[1]:
    print("you win!")
elif user_choice == choice[0] and computer_choice == choice[2]:
    print("you win!")
elif user_choice == choice[2] and computer_choice == choice[1]:
    print("you win!")
else:
    print("you lost")