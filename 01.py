# ÜL 01 joonistan kolmnurga
# impordin turtle sisse, näitan ja kuju(turtle)

import turtle
turtle.showturtle()
turtle.shape("turtle")

#asukoha vahetus

turtle.speed(0) #kiirus
turtle.penup()  #pen ülesse
turtle.goto(-100,200) #määran asukoha
turtle.pendown()     #pen alla

#kuhu liigub(test kolmnurk)

turtle.left(30)  #liigub vasakule(kraadides)
turtle.forward(200) #liigub otse(pikslites)
turtle.left(90)
turtle.forward(200)
turtle.left(135)
turtle.forward(283)

#süda
turtle.penup()  #pen ülesse
turtle.goto(200,200) #määran asukoha
turtle.pendown()
turtle.left(120)
turtle.forward(100)
turtle.circle(50,180)
turtle.right(90)
turtle.circle(50,180)
turtle.forward(105)

# lõpetab koodi
turtle.done()
