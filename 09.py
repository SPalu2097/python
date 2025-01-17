#Ülesanne 9 
#17.01.2025

# import random

# # for i in range(1,21):
# #     print(f"{i}.", end=" ")
# #     print(random.randint(1,22))
# numbrid = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]

# paaris=[]
# paaritu=[]
# for nr in numbrid:
#     if nr%2==0:
#         paaris.append(nr)
#     else:
#         paaritu.append(nr)

# print(paaris)
# print(paaritu)

# for i in range(43):
#     #print(i)
#     if i%3==0 and i%5==0:
#         print(f"{i} TIKTAK")
#     elif i%3==0:
#         print(f"{i} TIK")
#     elif i%5==0:
#         print(f"{i} TAK")
#     else:
#         print(i)

# for a in range(1,6):
#     print(" " *a, end=" ")
#     print("*" * (6-a))

# ev_data = [
# ['vehicle', 'range', 'price'],
# ['Tesla Model Y Long Range', '330', '58990'],
# ['Volkswagen ID.4 Pro', '260', '39995'],
# ['Ford Mustang Mach-E', '300', '42995'],
# ['Audi e-tron GT', '238', '102700'],
# ['Nissan Leaf', '149', '27400'],
# ['BMW iX xDrive50', '324', '83995'],
# ['Polestar 2', '265', '45500'],
# ['Kia EV6 Long Range', '310', '47795'],
# ['Mercedes-Benz EQS 450+', '350', '102310'],
# ['Hyundai Kona Electric', '258', '37400']
# ]
# avgRange = []
# #print(ev_data[0][0])
# for autod in ev_data:
#     print(f"{autod[0]:30}   {autod[1]:5}   {autod[2]:30}")
#     if autod[1].isnumeric():
#         avgRange.append(int(autod[1]))
#     # for i in autod:
#     #     print(i)
# print(f"Keskmine ulatus: {sum(avgRange)/len(avgRange)}")

# for autod in ev_data:
#     if autod[1].isnumeric():
#         if int(autod[1]) > 300:
#             print(autod[0])

import turtle 

import turtle

# Seadistame ekraani
screen = turtle.Screen()
screen.bgcolor("white")

# Loome turtli
t = turtle.Turtle()
t.speed(3)

# Funktsioon maja joonistamiseks
def draw_house(size):
    # Joonista maja põhja osa (ruut)
    for _ in range(4):
        t.forward(size)
        t.left(90)

    # Joonista katuse osa (kolmnurk)
    t.forward(size)
    t.left(45)
    t.forward(size / 2**0.5)  # Katuse ülemine külg
    t.left(90)
    t.forward(size / 2**0.5)  # Katuse teine külg
    t.left(45)

# Alguspunkt
t.penup()
t.goto(-200, -100)  # Liigutame turtli alguspunkti
t.pendown()

# Joonista 5 maja, kus suurus kasvab ja siis kahandab
for i in range(5):
    draw_house(50 + i * 20)  # Maja suurus kasvab
    t.penup()
    t.forward(100)  # Liigutame turtli järgmisse kohta
    t.pendown()

# Muutame turtli asukohta ja alustame kahaneva suurusega majade joonistamist
t.penup()
t.goto(-200, -200)
t.pendown()

for i in range(5):
    draw_house(150 - i * 20)  # Maja suurus kahandab
    t.penup()
    t.forward(100)  # Liigutame turtli järgmisse kohta
    t.pendown()

# Lõpetame joonistamise
t.hideturtle()

# Hoidke akent lahti
turtle.done()
