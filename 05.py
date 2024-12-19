#kommenteerimine: Ül on """ """ vahel ja kood aktiivseks ning alt+3 ning tulevad trellid
"""
Sa oled loomas programmi, mis aitab kontrollida, kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
Programm palub kasutajal sisestada oma vanuse. Kui vanus on vähemalt 18 aastat, siis programm annab teada, et kasutaja võib üritusele siseneda. Kui vanus on alla 18, siis programm teatab, et üritusele sisenemiseks ei ole piisavalt vana.
Kasuta if ja else lauseid, et luua see vanusekontrolli programm.
"""
# try:
#     vanus = int(input("Kui vana sa oled: "))
# 
#     if vanus >= 18:
#         print("Oled tere tulnud")
#     else:
#         print("Oled liiga noor")
# except:
#     print("Viga, sisestuses!")

"""
Sinu ülesanne on luua lihtne Pythoni programm, mis aitab kasutajal valida sobiva riietuse vastavalt ilmale.
Kasutaja sisestab temperatuuri (Celsius). Kui temperatuur on alla 0 kraadi, peab programm väljastama soovituse kanda talveriideid.
Kui temperatuur on vahemikus 0 kuni 15 kraadi, peaks programm soovitama kanda kevad-sügis rõivaid. Kui temperatuur on üle 15 kraadi, soovitab programm kanda suveriideid.
Kasuta if, elif ja else lauseid selle ülesande lahendamiseks.
"""
# try:
#     kraadid = int(input("Sisesta kraadid: "))
#     
#     if kraadid < 0:
#         print("Talve riided")
#     elif kraadid >= 0 and kraadid <= 15:
#         print("kevad/sügis riided")
#     else:
#         print("Pane lühkarid")
# except:
#     print("vale sisestus")

"""
Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse. Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”, kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.
"""
# import random
# 
# 
# 
# try:
#     arv1 = random.randint(1, 10)
#     arv2 = random.randint(1, 10)
#     vastus = int(input(f"{arv1} * {arv2} = "))
#     korrutis = arv1 * arv2
#     if korrutis == vastus:
#         print("Korrektne!")
#     else:
#         print("vale")
#     
# 
#     
# except:
#     print("Viga on sees!")

"""
Kirjuta programm, mis simuleerib mündiviskamist. Programm genereerib juhusliku tulemuse – “kiri” või “kull”, kasutades random.randint(0,1) funktsiooni.
Programmi koostamisel pead importima import random mooduli ja kasutama randint() funktsiooni, et valida kahe võimaliku tulemuse vahel.
Näiteks, kui randint(0, 1) annab tulemuseks 0, siis võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti. Kui arvas õigesti, siis joonista Turtle abil roheline ring; kui valesti, siis punane ring.
"""
try:

    import random
    import turtle

    valik = random.randint(0, 1)


    arvamus = int(input("Sisesta kas kull = 0 ja kiri = 1:"))
    
    if arvamus >=0 and arvamus <=1:
        if arvamus == valik:
            turtle.color("green")
            turtle.circle(50)
            
        else:
            turtle.color("red")
            turtle.circle(50)
            
        turtle.done()
    else:
        print("sellist numbrit ei ole")
    

except:
    ("sisesta korrektne tekst")



























