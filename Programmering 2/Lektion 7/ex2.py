class Djur:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def äta(self):
        print(f"{self.namn} äter.")

    def sova(self):
        print(f"{self.namn} sover.")

    def göra_ljud(self):
        print(f"{self.namn} gör ett ljud.")


class Hund(Djur):
    def __init__(self, namn, ålder, ras): # ras (breed på engelska)
        # super() används för att anropa en metod från basklassen (Djur) i en subklass (Hund).
        super().__init__(namn, ålder)   # super().__init__() betyder kör init metoden för klassen Djur (basklassen).
        self.ras = ras # En unik egenskap som finns bara för hundar i detta program, inte för alla djur. 

    def skälla(self):           # Denna metod finns bara för hundar, inte för övriga djur.
        print(f"{self.namn} skäller.")
        
        # Ersätta göra_ljud metoden i Djur-klassen
    def göra_ljud(self):
        self.skälla()
        
       # Ny metod för att skriva ut hundens ras
    def visa_ras(self):
        print(f"{self.namn} är av rasen {self.ras}.")


        
#from ex2_classes import * # importera alla klasser. Eller from ex2_classes import Djur, Hund
def main():
    djur = Djur("Djuret", 5)
    djur.äta()  # object.method()
    djur.sova()
    djur.göra_ljud()

    hund = Hund("Fido", 3, "Labrador")
    hund.äta()  # object.method()
    hund.sova()
    hund.göra_ljud()
    hund.visa_ras()  # Skriv ut rasen för hunden

main() 

