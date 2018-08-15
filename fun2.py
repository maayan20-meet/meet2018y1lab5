import turtle
turtle.goto(0,0)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = None


def up():
    global direction
    print("You pressed the up key.")
    direction = UP
    on_move()

def down():
    global direction
    print("you pressed the down key")
    direction = DOWN
    on_move()

def left():
    global direction
    print("you pressed the left key")
    direction = LEFT
    on_move()

def right():
    global direction
    print("you pressed the right key")
    direction = RIGHT
    on_move()

def space():
    if turtle.isdown():
        turtle.up()
    else:
        turtle.down()

    
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space")


turtle.listen()

def on_move():
    
    x_change = 10
    y_change = 10
    (x,y) = turtle.position()
    if direction == UP:
        turtle.goto(x,y + y_change)
    if direction == DOWN:
        turtle.goto(x,y - y_change)
    if direction == RIGHT:
        turtle.goto(x + x_change, y)
    if direction == LEFT:
        turtle.goto(x - x_change, y)





    
    
