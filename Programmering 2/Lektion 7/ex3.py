class Fordon:
    def __init__(self, märke, modell, år):
        self.märke = märke  # "Märke" syftar på tillverkaren
        self.modell = modell
        self.år = år  

    #def visa_info(self):
       # return f"Märke: {self.märke}, Modell: {self.modell}, År: {self.år}"  # Returnerar fordonets information

# Barnklass som ärver från Fordon-klassen
class Bil(Fordon):
    def __init__(self, märke, modell, år, antal_dörrar):
        super().__init__(märke, modell, år)  # Anropar föräldraklassens __init__
        self.antal_dörrar = antal_dörrar  # "Antal_dörrar" syftar på antalet dörrar på bilen.

    def visa_info(self):
        return f"Märke: {self.märke}, Modell: {self.modell}, År: {self.år}, Dörrar: {self.antal_dörrar}"  # Returnerar bilens information

# Fråga användaren om fordonsinformation
märke = input("Ange fordonets märke: ")
modell = input("Ange fordonets modell: ") 
år = input("Ange fordonets år: ") 
dörrar = input("Ange antalet dörrar för fordonet: ") 

# Skapa en bilinstans
bil = Bil(märke, modell, år, dörrar)  # Skapar en instans av klassen Bil
# Visa information om bilen
print("\nFordonsinformation:")  
print(bil.visa_info())  # Skriver ut bilens information
