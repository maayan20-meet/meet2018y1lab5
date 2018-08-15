##In order complete this challenge you need to debug the following code.
##It may be easier to do so if you improve the code quality. 

import turtle

yp7 = turtle.Turtle()
t = 200
b = -200

#draw A

turtle.hideturtle()





yp7.penup()

a,c = yp7.pos()

yp7.goto(a,c)

yp7.pendown()
yp7.goto(a+100, c+300)
yp7.goto(a+200, c)
yp7.penup()
yp7.goto(a+30, c+100)
yp7.pendown()

yp7.goto(a+175, c+100)

turtle.manloop()

