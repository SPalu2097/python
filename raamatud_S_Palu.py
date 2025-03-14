# Leia, mitu raamatut ilmus enne 2000. aastat.
# 	Leia kõik raamatud, mis pole saadaval.	
#     Leia vanim raamat andmestikus.
# 	Leia zanr, mida esineb andmetes kõige sagedamini.
# 	Leia, mitu raamatut on välja antud pärast aastat 2010.

import requests

url = "https://metshein.com/kordamine/json/raamatud.json"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    raamatud = data.get("raamatud", [])
    #print(raamatud)
    no_saadavus= []
    mitu_raam_2010 = 0
   
    for raamat in raamatud:
        if raamat['saadavus'] == False:
            no_saadavus.append(raamat)
    for i in no_saadavus:
        print(i['pealkiri'])
    


            
    
else:
    print("Error ei saa infot kätte ")
