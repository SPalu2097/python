#ülesanne 3 värvid
#importin turtle ja joonistan olümpia rõngad
import turtle

"""
    Loo aken, mille nimi on “Olümpiarõngad ja sinu nimi”
    Akna suurus 500×400
    Loo värvilised 50px olümpiarõngad (sinine, must, punane, kollane, roheline)
    Joone paksus 6
    Kiirus 0
"""
#akna seaded 
aken = turtle.Screen()
aken.setup(width=530,height=500)
aken.title("Olümpiarõngad, Simon Palu")
#sinine
turtle.speed(0)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.color("blue")
turtle.pensize(10)
turtle.circle(50,360)
turtle.penup()
#must
turtle.speed(0)
turtle.penup()
turtle.goto(-90,100)
turtle.pendown()
turtle.color("black")
turtle.pensize(10)
turtle.circle(50,360)
turtle.penup()
#punane
turtle.speed(0)
turtle.penup()
turtle.goto(20,100)
turtle.pendown()
turtle.color("red")
turtle.pensize(10)
turtle.circle(50,360)
turtle.penup()
#roheline
turtle.speed(0)
turtle.penup()
turtle.goto(-35,40)
turtle.pendown()
turtle.color("green")
turtle.pensize(10)
turtle.circle(50,360)
turtle.penup()
#kollane
turtle.speed(0)
turtle.penup()
turtle.goto(-150,40)
turtle.pendown()
turtle.color("yellow")
turtle.pensize(10)
turtle.circle(50,360)
turtle.penup()






turtle.done()