class Stadion:
    def __init__(self,stadion:str, varos:str, csapatok_szama:int, elso_merkozes:str, utolso_merkozes:str):
        self.stadion = stadion
        self.varos = varos
        self.csapatok_szama = csapatok_szama
        self.elso_merkozes = elso_merkozes
        self.utolso_merkozes = utolso_merkozes

    def __str__(self):
        txt = f"{self.stadion}, {self.varos}, {self.csapatok_szama}, {self.elso_merkozes}, {self.utolso_merkozes}"
        return txt