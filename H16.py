import os
from datetime import date

print(os.name)

print(f" Tere! {os.getlogin()}, tore sind jälle näha!")

print(f" Sinu töötav kataloog {os.getcwd()} ")
#alg väärtusete lisamine
kataloogidearv = 10 
kustuta = 5
#määrame muutuja tänase kuupäevaga
kp = str(date.today())
#loome kataloogi tänase kuupäevaga ja selle sisse 1-10 kaustad
try:
    os.mkdir(kp)
    print(f"{kp} kataloog on loodud")

    for i in range(1, kataloogidearv+1):
        kaust = kp +"/"+str(i)
        print(kaust)
        os.mkdir(kaust)
except:
    print("Kataloog juba olemas")
#kustutab kataloogi
if os.path.exists(kp +"/"+str(kustuta)):
    os.rmdir(kp +"/"+str(kustuta))
    print(f"{kustuta} kataloog kustutatud!")
else:
    print(f"{kustuta} kataoogi ei leitud!")

#kuvab kataloogi
dir_list = os.listdir(kp)
print("Kataloogi sisu: ")
for i in dir_list:
    print(i)