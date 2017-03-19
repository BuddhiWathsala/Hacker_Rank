import turtle

turtle.penup()
turtle.goto(-75,150)
turtle.pendown()
turtle.begin_fill() # Begin to fill color 
turtle.color("black")
turtle.circle(10) #eye one
turtle.end_fill()#end filling

turtle.penup()
turtle.goto(75,150)
turtle.pendown()
turtle.begin_fill() # Begin to fill color 
turtle.color("black")
turtle.circle(10) #eye two 
turtle.end_fill()#end filling

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(100,80)   #right smile

turtle.penup()           
turtle.setheading(180) 
turtle.goto(0,0)
turtle.pendown()
turtle.circle(-100,80) #left smile

turtle.penup()
turtle.goto(150,125)
turtle.pendown()
turtle.circle(150) #face

turtle.done()


