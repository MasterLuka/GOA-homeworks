from turtle import*
#we want to paint a house
#step 1: draw a square 
speed(3)
width(7)

color("blue")
forward(200)
left(90)
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square
forward(70)
left(90)
color("red")
forward(120)
right(90)
forward(60)
right(90)
forward(120)

color("gold")
penup()
goto(200 , 200)
pendown()
right(150)
forward(200)
left(120)
forward(200)

penup()
goto(50 , 100)
color("orange")
pendown()
left(30)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)

#end of window N.1

penup()
goto(150,100)
color("orange")
pendown()
right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)

#end of window N.2

penup()
goto(120 , 190)
color("orange")
pendown()
left(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)

exitonclick()