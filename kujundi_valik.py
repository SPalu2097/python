from turtle import *
import random


def viisnurk():
    for _ in range(5):
        forward(100)
        right(72)
    liigu_edasi()

def ruut():
    for _ in range(4):
        forward(100)
        right(90)
    liigu_edasi()

def ring():
    circle(50)
    liigu_edasi()

def suvaline():
    random.choice([viisnurk, ruut, ring])() 

def liigu_edasi():
    """Liigutab pliiatsi järgmise kujundi alguskohta."""
    penup()
    forward(200)
    pendown()


while True:
    try:
        kujund = input("Palun valige kujund (viisnurk, ring, ruut, suvaline): ")
        arv = int(input("Mitut kujundit te soovite: "))

        if kujund in ["viisnurk", "ruut", "ring", "suvaline"]:
            for _ in range(arv):
                if kujund == "viisnurk":
                    viisnurk()
                elif kujund == "ruut":
                    ruut()
                elif kujund == "ring":
                    ring()
                else:
                    suvaline()
        else:
            print("Vale väärtus! Proovi uuesti.")

        
        jatka = input("Kas soovid anda uued väärtused (jah/ei): ")
        if jatka != "jah":
            break

    except:
        print("Ilmnes viga!")

done()

