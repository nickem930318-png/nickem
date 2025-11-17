# fil: klasser.py
class Person:
    def __init__(self, namn, alder):
        self.namn = namn
        self.alder = alder

class Lärare(Person):
    def __init__(self, namn, alder, ämne):
        super().__init__(namn, alder)
        self.ämne = ämne

    def presentera(self):
        print(f"Jag heter {self.namn}, är {self.alder} år och undervisar i {self.ämne}.")
        
        
        # fil: main.py
from klasser import Lärare

lärare1 = Lärare("Anna", 45, "matematik")
lärare1.presentera()

