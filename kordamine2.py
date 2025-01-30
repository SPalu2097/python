import random
# 2.1 äratus, küsi arvu kasutajalt ja nii mitu korda talle kuvatakse teksti "Tõuse ja sära!"

# try:

#     kordus = int(input("Mitu korda äratus heliseb: "))

#     i = 0
#     while i < kordus:
#         i = i + 1
#         print("Tõuse ja sära!")

# except:
#     print("Sisesta täis arv!!!")    


# MURELIKUD LAPSEVANEMAD
# Jänesevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel porgandeid juurde ei saa. 

# Koostada programm, mis
# küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.
# Näiteks, kui kasutaja sisestas 6, siis summa on 12, sest 2 + 4 + 6 = 12. Kui kasutaja sisestas 7, siis on summa samuti 12, sest 2 + 4 + 6 = 12.
# Näited programmi tööst:


# try:

#     ring = int(input("kui mitu ringi jänkud jooksid: "))

#     porgand = 0 

#     while ring > 0:
#       #print(ring)
#        if ring % 2 == 0:
#            porgand += ring
#        ring-=1
        

#     print(porgand)

# except:
#     print("sisesta ainult täis arvud!")

# 2.5 ÕUNAD
# Lumivalgekesel oli 14 õuna ja ta tahtis neid pöialpoistega jagada. Ta sai aru, et kui kõik seitse pöialpoissi tahavad õunu ja ta annaks kõigile kaks õuna, jääks ta ise üldse ilma. Nüüd otsustas ta õunu jagada nii, et küsib, mitu pöialpoissi tahab õunu, ja seejärel loosib iga soovija korral, kas anda talle üks või kaks õuna. Koostada programm, mis
# küsib kasutajalt, mitu pöialpoissi tahab õunu (võib eeldada, et sisestatakse täisarv lõigust [0; 7]);
# leiab ja väljastab eraldi ridadele, mitu õuna saab iga pöialpoiss (programm genereerib iga kord juhuslikult arvu 1 või 2);
# leiab ja väljastab eraldi reale, mitu õuna jääb Lumivalgekesele.

# ounad = 14
# pp = int(input("Mitu PP tahab õuna: "))

# for i in range(pp):
#     suv_oun = random.randint(1,2)
#     print(suv_oun)
#     ounad -= suv_oun
# print(f"Lumivalgkekesele jäi: {ounad} õuna")

