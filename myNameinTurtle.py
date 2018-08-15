import turtle

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-350,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-350,-100+200) 
turtle.goto(-350+50,-100) 
turtle.goto(-350+100,-100+200)
turtle.goto(-350+100,-100)

firstA = -200
secondA = -50
thirdA = 250 

turtle.penup()

turtle.goto(firstA,-100)

turtle.pendown()

turtle.goto(firstA+50,100)
turtle.goto(firstA+100,-100)
turtle.goto(firstA+75,0)
turtle.goto(firstA+25,0)

turtle.penup()

turtle.goto(secondA,-100)

turtle.pendown()

turtle.goto(secondA+50,100)
turtle.goto(secondA+100,-100)
turtle.goto(secondA+75,0)
turtle.goto(secondA+25,0)

turtle.penup()

turtle.goto(150,-100)

turtle.pendown()

turtle.goto(150,0)
turtle.goto(100,100)
turtle.goto(150,0)
turtle.goto(200,100)

turtle.penup()

turtle.goto(thirdA,-100)

turtle.pendown()

turtle.goto(thirdA+50,100)
turtle.goto(thirdA+100,-100)
turtle.goto(thirdA+75,0)
turtle.goto(thirdA+25,0)

turtle.penup()

turtle.goto(400,-100)

turtle.pendown()

turtle.goto(400,100)
turtle.goto(475,-100)
turtle.goto(475,100)














