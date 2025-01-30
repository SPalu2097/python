# 2.1 äratus, küsi arvu kasutajalt ja nii mitu korda talle kuvatakse teksti "Tõuse ja sära!"

try:

    kordus = int(input("Mitu korda äratus heliseb: "))

    i = 0
    while i < kordus:
        i = i + 1
        print("Tõuse ja sära!")



except:
    print("Sisesta täis arv!!!")    