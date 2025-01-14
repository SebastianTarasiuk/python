class Miejscowosc:
    def __init__(self, nazwa, liczba, powierzchnia):
        self.nazwa = nazwa
        self.liczba = liczba
        self.powierzchnia = powierzchnia

class Miasto(Miejscowosc):
    def __init__(self, nazwa, liczba, powierzchnia, prezydent, powiat):
        super().__init__(nazwa, liczba, powierzchnia)
        self.prezydent = prezydent
        self.powiat = powiat


class Wies(Miejscowosc):
    def __init__(self, nazwa, liczba, powierzchnia, soltys, gmina):
        super().__init__(nazwa, liczba, powierzchnia)
        self.soltys = soltys
        self.gmina = gmina

miasto = Miasto("Warszawa", 1800000, 517, "Rafał Trzaskowski", "mazowieckie")
wies = Wies("Zawoja" , 7500, 454, "Adam", "suski")

print(miasto)
print(wies)