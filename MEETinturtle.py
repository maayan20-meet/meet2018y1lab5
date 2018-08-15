import turtle
firstE = -50

secondE = 100

# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...
turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

turtle.penup()

turtle.goto(firstE,-100)

turtle.pendown()

turtle.goto(firstE,100)
turtle.goto(firstE+75,100)
turtle.goto(firstE,100)
turtle.goto(firstE,0)
turtle.goto(firstE+75,0)
turtle.goto(firstE,0)
turtle.goto(firstE,-100)
turtle.goto(firstE+75,-100)

turtle.penup()

turtle.goto(secondE,-100)

turtle.pendown()

turtle.goto(secondE,100)
turtle.goto(secondE+75,100)
turtle.goto(secondE,100)
turtle.goto(secondE,0)
turtle.goto(secondE+75,0)
turtle.goto(secondE,0)
turtle.goto(secondE,-100)
turtle.goto(secondE+75,-100)

turtle.penup()

turtle.goto(300,-100)

turtle.pendown()

turtle.goto(300,100)
turtle.goto(225,100)
turtle.goto(375,100)

# ...and end it before the next line.
turtle.mainloop()
