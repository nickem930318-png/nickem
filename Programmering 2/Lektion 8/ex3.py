
class Djur:
    def __init__(self, art, ljud):
        self.art = art  
        self.ljud = ljud  

    def göra_ljud(self):
        return f"{self.art.capitalize()} gör ett {self.ljud}-ljud."  # Returnerar en sträng med djurets art och ljud.
    # capitalize()-metoden för att ändra den första bokstaven i en sträng till versal (stor bokstav) och resten av bokstäverna till gemener (små bokstäver).

# Barnklass som ärver från Djur-klassen
class Hund(Djur):
    def __init__(self, namn):
        super().__init__("hund", "skäll")  # Anropar föräldraklassens __init__ med "hund" och "skäll"
        self.namn = namn  # Initierar instansvariabeln namn med värdet av namn

    def hälsa(self):
        return f"{self.namn} viftar på svansen och säger: {self.ljud.capitalize()}!"  # Returnerar en sträng med hundens namn och ljud

# Barnklass som ärver från Djur-klassen
class Katt(Djur):
    def __init__(self, namn):
        super().__init__("katt", "mjau")  # Anropar föräldraklassens __init__ med "katt" och "mjau"
        self.namn = namn  # Initierar instansvariabeln namn med värdet av namn

    def hälsa(self):
        return f"{self.namn} spinner mjukt och säger: {self.ljud.capitalize()}."  # Returnerar en sträng med kattens namn och ljud
        
        

# Skapa instanser av de olika djuren
hund = Hund("Bobi")  
katt = Katt("Mimi")  

# Visa hur djuren låter och hälsar
print(hund.göra_ljud())  # Skriver ut hur hunden låter
print(hund.hälsa())  # Skriver ut hur hunden hälsar
print(katt.göra_ljud())  # Skriver ut hur katten låter
print(katt.hälsa())  # Skriver ut hur katten hälsar