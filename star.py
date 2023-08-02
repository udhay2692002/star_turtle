import turtle
turtle.hideturtle()
turtle.pen(pencolor="green", pensize=3)
turtle.speed(10)
turtle.begin_fill()
for i in range(5):
    turtle.forward(250)
    turtle.right(144)
    turtle.fillcolor("pink")
turtle.end_fill()


