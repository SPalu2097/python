import turtle

#seaded
kylje_pikkus = 120
nurk = 120
varv = "blue"
varv2 = "red"

#kolmnurk
turtle.color(varv)
turtle.forward(kylje_pikkus) 
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)

#edasi liikumine
turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

#järgmine kolmnurk
turtle.color(varv2)
turtle.forward(kylje_pikkus) 
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)

#liigun edasi
turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

#järgmine kolmnurk
turtle.color(varv)
turtle.forward(kylje_pikkus) 
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)



turtle.done()