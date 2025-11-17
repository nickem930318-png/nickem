class Bicycle:# self måste alltid vara första parametern i alla metoder. Detta är för att berätta till programmet att metoden tillhör ett object i klassen.
    # Metoden `__init__`: används för att initialisera nyskapade objekt från en klass med startvärden. 
    def __init__(self, brand, model, year, gear_count): # init method
        # attribut = parameter
        self.brand = brand
        self.model = model
        self.year = year
        self.gear_count = gear_count # antalet tillgängliga växlar på cykeln.

    def change_gears(self, new_gear): # Method
        self.gear_count = new_gear

    def display_info(self): # Method
        return f"{self.brand} {self.model}, {self.year} model, with {self.gear_count} gears."

# Skapa object / instanser
bike1 = Bicycle("Trek", "Marlin 7", 2023, 21)
bike2 = Bicycle("Giant", "Talon 1", 2022, 24)

# Ändra växlar och visa information
bike1.change_gears(18)
print(bike1.display_info())
print(bike2.display_info())

