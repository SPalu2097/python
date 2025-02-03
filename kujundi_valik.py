# KILPKONN
# Kirjuta programm, mis lubab kasutajal valida kujundite tüübi 
# (viisnurk, ring, ruut või suvaline) ja arvu. 
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul,
#  kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Näide:
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist,
#  jättes sisendi tühjaks.

from turtle import *
import random
try:
    while True:
        kujund = str(input("Palun valige millist kujundit tahate(viisnurk, ring, ruut, suvaline):  "))

        arv = int(input("Mitut kujundit te soovite:  "))

        def kujuke():
            if kujund == "viisnurk":
                viisnurk()
            elif kujund == "ruut":
                ruut()
            elif kujund == "ring":
                ring()
            elif kujund == "suvaline":
                suvaline()
            else:
                print("Vale väärtus!!!")

        def viisnurk():
            for i in range(5):
                forward(100)
                right(72)
            penup()
            forward(200)
            pendown()

        def ruut():
            for i in range(4):
                forward(100)
                right(90)
            penup()
            forward(200)
            pendown()

        def ring():
            r = 50
            circle(r)
            penup()
            forward(200)
            pendown()

        def suvaline():
            mylist = ["viisnurk", "ruut", "ring"]
            vastus = random.choice(mylist)
            #print(vastus)
            if vastus == "viisnurk":
                viisnurk()
            elif vastus == "ruut":
                ruut()
            else:
                ring()



        for f in range(arv):
            kujuke()
        
        jatka = str(input("Kas soovid anda uued väärtused(jah/ei): "))
        if jatka == "jah":
            continue
        elif jatka == "ei":
            break
        else:
            print("Sisestasid vale väärtuse!")
            break
        

except:
    print("Sa ajasid midagi väga sassi!!!")

done()