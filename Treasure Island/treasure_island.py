print('\n')
greetings = f"Welcome to treasure Island\n"
print(greetings)

mission = f"Your mission is to find treasure\n"
print(mission)

option1 = input("You're at cross road where do you want to go? Type left or right: \n").lower()

if option1 == "left":
    option2 = input('You have come to a lake there is an Island in the middle of the lake. Type "wait" to wait for a '
                    'boat. Type "swim" to swim across:.\n').lower()
    if option2 == "wait":
        option3 = input(
            "You arrived at the Island unharmed. There is a door with three doors. One red, one yellow and one blue. Which color do you choose:\n").lower()

        if option3 == "red":
            print("It is a room full of fire. Game over")
        elif option3 == "yellow":
            print("You have found the treasure! You won!")
        elif option3 == "blue":
            print("You enter a room of beast. Game over!")
        else:
            print("You chose a door that does not not exist. Game over!")
    else:
        print("You get attacked by an angry trout. Game over")
else:
    print("You fell into a hole. Game over!")
