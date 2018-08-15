import turtle # python needs this to use all the turtle functions
turtle.shape('turtle') # changes the shape to a turtle
finn = turtle.clone() # creates new turtle and saves it in finn
finn.shape('square') # changes shape of 2nd turtle to square

finn.goto(100,100) # moves square to (x=100,y=100)
finn.pendown()


finn.forward(100)
finn.left(90)
finn.forward(100)
finn.left(90)
finn.forward(100)
finn.left(90)
finn.forward(100)
finn.left(90)

charlie = turtle.clone()
charlie.shape('triangle')

charlie.goto(50,100)
charlie.goto(100,0)
charlie.goto(0,0)

finn.goto(300,300)
finn.stamp()
finn.goto(100,100)

charlie.goto(-300,-300)
charlie.stamp()
charlie.goto(0,0)
