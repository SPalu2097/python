#3.ülesanne
#muutujad

nimi = "Imre" #sõne, string, str
pere_nimi = "Tard"
vanus = 20 #täisarv, integer, int
keskmine_hinne = 4.53 #komaarv, float

print(type(nimi))
print(type(vanus))
print(type(keskmine_hinne))
#niimoodi saab lauseid ehitada
print(nimi+","+str(vanus)+" aastat vana "+" kelle, keskmine hinne on "+ str(keskmine_hinne))
print(nimi,",",vanus,"aastat vana ja kelle keskmine hinne on",keskmine_hinne)
#lause vormindamine
print(f" {nimi} {pere_nimi}, on {vanus} aastat vana ja kelle keskmine hinne on {keskmine_hinne}")
