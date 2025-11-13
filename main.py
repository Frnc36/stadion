from Stadion import Stadion
import feladatok

stadion_lista = []

def fajlbeolvasas():
    f = open("stadionok.txt", "r", encoding="UTF-8")
    f.readline()
    szoveg_lista = f.readlines()
    f.close

    i = 0
    while i < len(szoveg_lista):
        sor = szoveg_lista[i].strip().split(";")
        stadion = Stadion(sor[0], sor[1], int(sor[2]), sor[3], sor[4])
        stadion_lista.append(stadion)
        i += 1
    
    i = 0
    while i < len(stadion_lista):
        print(stadion_lista[i])
        i += 1
    return stadion_lista

lista = fajlbeolvasas()


york = feladatok.hany_new_york(lista)
print("\n1.feladat")
print(f"New York-ban: {york} stadion van.")

ossz = feladatok.ossz_csapat(lista)
print("\n2.feladat")
print(f"Összesen: {ossz} csapat van.")

print("\n3.feladat")
feladatok.elott_volt_1900_01_01(lista)

print("\n4.feladat")
db = feladatok.kettoezer_ota(lista)
print(f"{db} stadion van.")

print("\n5.feladat")
buffalo = feladatok.buffalo(lista)
print(f"Ennyi volt: {buffalo}")