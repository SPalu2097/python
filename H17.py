tehingute_arv = 0
positiivsete_tehingute_arv= 0
pos_arv_summa= 0

with open("pangakonto.txt") as fail:
    sisu = fail.readlines()
    for number in sisu:
        #print(float(number))
        tehingute_arv+=1
        if float(number) > 0:
            positiivsete_tehingute_arv+=1
            pos_arv_summa += float(number)

print(f"Tehingute arv: {tehingute_arv}")
print(f"Positvsete tehingute arv: {positiivsete_tehingute_arv}")
print(f"Positvsete tehingute summa: {pos_arv_summa:.2f}")

#see on teine ülesanne
meeste_keskmine_palk = 0
naiste_keskmine_palk = 0
mpalgad = 0
with open("palgad.txt") as fail:
    sisu2 = fail.readlines()
    for i in sisu2:
        #print(i, end="")
        tykeldus = i.split(",")
        if tykeldus[3] == "Mees":
            mpalgad+=float(tykeldus[6])
print(f"Meeste palgad: {mpalgad:.2f}")