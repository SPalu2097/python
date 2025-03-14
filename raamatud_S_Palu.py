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
    mitu_raamat = []
    vanim_raamat = raamatud[0]
    #print(vanim_raamat['väljaandmise_aasta'])
   
    for raamat in raamatud:
        if raamat['saadavus'] == False:
            no_saadavus.append(raamat)
    for i in no_saadavus:
        print(i['pealkiri'])
    
    for r in raamatud:
        if r['väljaandmise_aasta'] >= 2010:
            mitu_raamat.append(r)
    print(f"Raamatuid, mis on välja antud alates 2010. aastast: {len(mitu_raamat)}")
            
    for raamat in raamatud:
        if raamat['väljaandmise_aasta'] < vanim_raamat['väljaandmise_aasta']:
            vanim_raamat=raamat
    #print(vanim_raamat)
    print(f"Vanim raamat on: {vanim_raamat['pealkiri']} {vanim_raamat['väljaandmise_aasta']} ")
    


            
    
else:
    print("Error ei saa infot kätte ")
