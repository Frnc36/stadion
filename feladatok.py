from datetime import datetime

def hany_new_york(lista):
    cv = 0
    york = 0
    while cv < len(lista):
        if lista[cv].varos == "New York":
            york += 1
        
        cv += 1
    return york


def ossz_csapat(lista):
    cv = 0
    ossz = 0
    while cv < len(lista):
        ossz += lista[cv].csapatok_szama
        cv += 1
    return ossz

def elott_volt_1900_01_01(lista):
    cv = 0
    datum = "1900-01-01"
    datum_objektum = datetime.strptime(datum, "%Y-%m-%d").date()
    while cv < len(lista):
        # datetime.strptime(lista[cv].elso_merkozes, "%Y-%m-%d").date()
        if datetime.strptime(lista[cv].elso_merkozes, "%Y-%m-%d").date() < datum_objektum:
            print(lista[cv].stadion)
        cv += 1

def kettoezer_ota(lista):
    cv = 0
    db = 0
    datum = "2000-01-01"
    datum_objektum = datetime.strptime(datum, "%Y-%m-%d").date()
    while cv < len(lista):
        if datetime.strptime(lista[cv].utolso_merkozes, "%Y-%m-%d").date() < datum_objektum:
            db += 1
        cv += 1
    return db   


def buffalo():
    