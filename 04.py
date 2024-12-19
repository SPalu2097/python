
# 4.1
"""
Kirjuta programm, mis aitab aiapidajal arvutada aia ymbermootu.
Aed on ristkyliku kujuline.
Programm peaks kysima kasutajalt kahe aiaosa pikkused meetrites ja seej2rel arvutama aia kogupikkuse.
V2ljasta lause, kasutades f-string vormindamist.
"""

a = int(input("sisesta kylg 1: "))
b = int(input("sisesta kylg 2: "))

ymbermoot = 2*(a+b)
#print(ymbermoot)
print(f"Aia kogu pikkus on {ymbermoot} meetrit")

#4.4
"""
Sa tootad kingipoes ja sinu ylesanne on pakkida kingitusi.
Igasse kinkekarpi mahub t2pselt 5 kingitust.
Sinu ylesandeks on arvutada, mitu t2is kinkekasti saad teha ja mitu kingitust j22b yle, kui need koik ei mahu karpidesse.
Loo programm, mis kysib kasutajalt, mitu kingitust on vaja pakkida.
Programm peaks seej2rel arvutama, mitu t2is kinkekasti saab teha ja mitu kingitust j22b yle. Kasuta t2isarvulist jagamist (//) kinkekarpide arvu leidmiseks ja j22gi (%) operaatorit ylej22vate kingituste arvu leidmiseks.
Kasuta veakontrolli ja vastuse vormindamist.
"""

try:
    karbi_suurus = 5
    kingitused = int(input("Lisa kingituste arv: "))

    kastid = kingitused//karbi_suurus
    jaak = kingitused % karbi_suurus
    print(f"Teha saab {kastid} t2is kinke kasti ja j22k on {jaak}")
except:
    print("J2lle tekitad probleeme!")

try:
    maht = int(input("Kui suur on su faili maht(MB): "))
    kiirus = int(input("Kui kiire on su andme edastus(MB/s):"))

    aeg = maht / kiirus
    print(f"Teie faili alla laadimiseks kulub {aeg} sekundit!")
except:
    print("Sisesta ilma komata arvud, palun!")
