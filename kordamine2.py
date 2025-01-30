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

# TÄRINGUD
# Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks on vaja 5 täringut, Crapsi jaoks aga 2 täringut. Koostada programm, mis
# küsib kasutajalt vajalike täringute arvu;
# viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis jäävad 1 ja 6 vahele);
# väljastab iga arvu eraldi reale.
# Vihje: Kui kasutada tsüklit, mis teeb kasutaja sisestatud arvu samme, siis igal sammul tuleb genereerida üks juhuslik arv ja see väljastada.

