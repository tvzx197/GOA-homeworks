from turtle import*

#we want to paint a house
#step1: draw a square

width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square
#draw a door

forward(70)
color("green") 
begin_fill()
left(90)

forward(120)   #height of the door
right(90)

forward(60)
right(90)

forward(120)
end_fill()

right(90)
left(180)

penup()
goto(190,0)
left(90)
color("brown")
begin_fill()
forward(130)
pendown()
forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)
end_fill()
left(90)
penup()
forward(130)
pendown()
color("brown")
begin_fill()
forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)
end_fill()
#end of windows

penup()
goto(200,200)
pendown()
color("purple")
begin_fill()
right(90)
left(30)
forward(200)
left(120)
forward(200)
end_fill()



exitonclick()