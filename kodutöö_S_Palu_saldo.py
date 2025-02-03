# PANGAKONTO
# Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt.
# Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone:
#  deposiit (raha lisamine)
#  väljavõte (raha eemaldamine)
# Tagastage peale igat toimingut konto jääk.
# Funtsiooni parameetrid:
#  algne_saldo: algse saldo väärtus
#  toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote')
#  summa: summa, mida soovitakse lisada või eemaldada

algne_saldo = 100


def deposiit():
     a = algne_saldo
     b = summa
     lopp_saldo= a+b
     print(f"Teie kontojaak on nüüd: {lopp_saldo}")

def valjavott():
    if algne_saldo >= summa:
        lopp_saldo = algne_saldo-summa
        print(f"Teie kontojääk on {lopp_saldo} €")
    elif algne_saldo < summa:
        print("Sinu arvel pole piisavalt vahendeid!!!")
    else:
        print("Oled sisestanud vale väärtuse")



print(f"Tere, Olen sinu pank ja sinu konto saldo on {algne_saldo}€ ")

valik = str(input("Tee oma valik: 'deposiit', 'valjavott' või 'exit'  "))

if valik == "deposiit":
    print("Valisid raha sisestamise!")
elif valik == "valjavott":
    print("Valisid raha valjavotmise")
elif valik == "exit":
    print("Valisid lahkumise")
    print("Head päeva Teile!")
    breakpoint
else:
    print("Kirjutasid midagi valesti")

summa = float(input("Kui palju raha: "))

if valik == "deposiit":
    deposiit()
elif valik == "valjavott":
    valjavott()
else:
    print("Sisestage palun õige väärtus valikust!")





