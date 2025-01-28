from turtle import *
 
speed(5)
penup()
goto(-200, 0)
pendown()

suurus = [1, 1.5, 2, 1.5, 1, 1.5]

def ehitame_maja(suurus=1):
    for i in range(4):
        pencolor("black")
        forward(20 * suurus)
        right(90)
    pencolor("green")
    left(45)
    forward(15 * suurus)
    right(90)
    forward(15 * suurus)
    penup()
    right(45)
    forward(20 * suurus)
    right(90)
    forward(5 * suurus)
    pendown()
    pencolor("blue")
    right(90)
    forward(15 * suurus)
    left(90)
    forward(10 * suurus)
    left(90)
    forward(15 * suurus)
    left(90)
    penup()
    forward(60)
    left(90)
    forward(20 * suurus)
    right(90)
    pendown()
 
 
ehitame_maja(suurus=1)
ehitame_maja(suurus=1.5)
ehitame_maja(suurus=2)
ehitame_maja(suurus=1.5)
ehitame_maja(suurus=1)
ehitame_maja(suurus=1.5)   


done()

