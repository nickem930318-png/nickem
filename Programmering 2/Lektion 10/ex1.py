class Bok:
    def __init__(self, titel, författare):
        self.titel = titel
        self.författare = författare
    def visa_info(self):
        return f"Titel: {self.titel}, Författare: {self.författare}"
    def läsa(self):
        return(f"Du läser {self.titel} av {self.författare}.")

class Ebok(Bok):
    def __init__(self, titel, författare, filstorlek):
        super().__init__(titel, författare)
        self.filstorlek = filstorlek
    
    def ladda_ned(self):
        return f"Du laddar ned {self.titel}. Filstorlek: {self.filstorlek} MB"
    
    def läsa(self):
        bas = super().läsa()
        return bas + " (på din surfplatta eller dator)"