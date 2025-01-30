musa = "edm.txt"
fail=open(musa, encoding="UTF-8")
nr=1
for pala in fail:
    print(str(nr)+"." +pala, end="")
    nr+=1

print()
valik = int(input("vali lugu: "))
fail= open(musa, encoding="UTF-8")
mangin = 1
for pala in fail:
    if valik == mangin:
        print(pala, end="")
    mangin +=1


fail.close()

#3.3
# Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud (kus positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). Iga arv on eraldi real. Tekstifaili kasutamiseks programmi sees peab fail asuma programmifailiga samas kaustas.
# Koostada programm, mis
# loeb failist nimega konto.txt andmed;
# väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis. 
# Näide programmi tööst:
# Näiteks antud näitefaili konto.txt puhul peab ekraanile ilmuma

# fail_konto = open("konto.txt" , encoding="UTF-8")

# for kirje in fail_konto:
#     if float(kirje) > 0:
#         print(float(kirje), end="\n")


#3.1 ülesanne
# Ülikooli vastuvõetud
# Ülikooli I õppeastmesse (bakalaureuseõpe jm) võetakse igal aastal vastu sadu inimesi. Viimastel aastatel vastuvõetud inimeste arvud on aastate kaupa failis rebased.txt, kus esimesel real on 2011. aastal vastuvõetute arv, teisel real 2012. aastal vastuvõetute arv kuni viimasel real on 2019. aastal vastuvõetute arv. 
# Koostada programm, mis
# loeb failist registreeritud vastuvõetute andmed aastate järgi järjendisse;
# Failist järjendisse saab lugeda järgmise programmijupi abil:
# küsib kasutajalt aastat
# võib eeldada, et sisestatakse täisarv, mis kuulub lõiku [2011; 2019].
# väljastab, mitu inimest sel aastal vastu võeti.
# Näide:
#   Palun sisestage, millise aasta andmeid vajate: 2011
#   2011. aastal oli vastuvõetuid 2803

# fail = open("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     #print(rida, end="")
#     vastuvõetud.append(int(rida))
# fail.close()
 
# # aasta = 1

# aasta = input("Lisa aasta 2011-2019: ")
# #print(aasta[3])
# print(vastuvõetud[int(aasta[3])-1])
