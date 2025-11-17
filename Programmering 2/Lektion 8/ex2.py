class Anställd:
    def __init__(self, namn, lön):
        self.namn = namn  # Initierar instansvariabeln namn med värdet av namn
        self.lön = lön  # Initierar instansvariabeln lön med värdet av lön

    def visa_info(self):
        return f"Namn: {self.namn}, Lön: {self.lön}"  # Returnerar information om den anställda

# Barnklass som ärver från Anställd-klassen
class Chef(Anställd):
    def __init__(self, namn, lön, avdelning):
        super().__init__(namn, lön)  # Anropar föräldraklassens __init__
        self.avdelning = avdelning  # Initierar instansvariabeln avdelning med värdet av avdelning

    def visa_info(self):
        return f"Namn: {self.namn}, Lön: {self.lön}, Avdelning: {self.avdelning}"  # Returnerar information om chefen
        



# Fråga användaren om information om en anställd
namn = input("Ange den anställdas namn: ")  
lön = input("Ange den anställdas lön: ") 
avdelning = input("Ange den anställdas avdelning: ") 

# Skapa en instans av chefklassen
chef = Chef(namn, lön, avdelning)  # Skapar en instans av klassen Chef

# Visa information om den anställda
print("\nAnställd information:")  # Skriver ut rubrik för anställd information
print(chef.visa_info())  # Skriver ut information om chefen
