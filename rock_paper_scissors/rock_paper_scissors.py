import random

rock = '👊'
paper = '🖐️'
scissors = '✌️'

game_images = [rock, paper, scissors]

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
    if user_choice >= 3 or user_choice < 0:
        print('You typed an invalid number, you lose!')
    else:
        print(game_images[user_choice])
    # user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
    # if user_choice.isdigit():
    # user_choice = int(user_choice)
    # print(int(game_images[user_choice]))
    # user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n'))
    # print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print('Computer chose:')
    print(game_images[computer_choice])

    # if user_choice >= 3 or user_choice < 0:
    #     print('You typed an invalid number, you lose!')

    if user_choice == 0 and computer_choice == 2:
        print('You win!')
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print('You win!')
    elif computer_choice == user_choice:
        print("It is a draw")

except ValueError:
    print('Invalid input. Please enter a valid number.')

# import random
#
# rock = '🪨'
# paper = '🖐️'
# scissors = '✂️'
#
# game_images = [rock, paper, scissors]
#
# try:
#     user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
#     if user_choice >= 3 or user_choice < 0:
#         print('You typed an invalid number, you lose!')
#     else:
#         print(game_images[user_choice])
#
#     computer_choice = random.randint(0, 2)
#     print('Computer chose:')
#     print(game_images[computer_choice])
#
#     if user_choice == 0 and computer_choice == 2:
#         print('You win!')
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print('You win!')
#     elif computer_choice == user_choice:
#         print("It is a draw")
#
# except ValueError:
#     print('Invalid input. Please enter a valid number.')
