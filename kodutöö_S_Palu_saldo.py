while True:
    saldo = 100


    print(f"Tere, Olen sinu pank ja sinu konto saldo on {saldo}€ ")

    try:
        valik = str(input("Tee oma valik: 'deposiit', 'valjavott' või 'exit'  "))
        
        def summaP():
            summa = float(input("Kui palju raha: "))
            return summa 


        if valik == "deposiit":
            print("Valisid raha sisestamise!")
            summa = summaP()
            saldoU = saldo + summa
            print(f"Teie kontojääk on {saldoU}€")
        elif valik == "valjavott":
            print("Valisid raha valjavotmise")
            summa = summaP()
            if saldo >= summa:
                saldoU=saldo - summa
                print(f"Teie kontojaak on {saldoU}€")
            elif saldo < summa:
                print("Arvel pole piisavalt raha")
            else:
                print("Sisesta numbrid!")
                breakpoint
        elif valik == "exit":
            print("Valisid lahkumise")
            print("Head päeva Teile!")
            breakpoint
        else:
            print("Kirjutasid midagi valesti")
            breakpoint
    except:
        print("Sisesta õigesti oma valik!")
    

    tegevus = int(input("Kas sulgen programmi? jah on 1 ja ei on 0: "))
    if tegevus != 0:
        break
