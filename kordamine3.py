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

fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    #print(rida, end="")
    vastuvõetud.append(int(rida))

fail.close()
# aasta = 1

aasta = input("Lisa aasta 2011-2019: ")
#print(aasta[3])
print(vastuvõetud[int(aasta[3])-1])