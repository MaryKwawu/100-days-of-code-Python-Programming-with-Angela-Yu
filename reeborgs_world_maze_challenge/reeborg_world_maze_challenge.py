
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while condition():
    move()

turn_left()

while not at_goal():
    if right_condition():
        turn_right()
        move()
    elif front_condition():
        move()
    else:
        turn_left()
