class Book:# self måste alltid vara första parametern i alla metoder. Detta är för att berätta till programmet att metoden tillhör ett object i klassen.
    # Metoden `__init__`: används för att initialisera nyskapade objekt från en klass med startvärden. 
    def __init__(self, title, author, year):# init method
        # attribut = parameter
        self.title = title 
        self.author = author
        self.year = year

    def describe(self):     # Method
        return f"{self.title} by {self.author}, published in {self.year}"
    

####### Outside class #######

# Skapa ett objekt/instans av klassen Bok
book1 = Book("The Stockholm City", "Pierre Gergi", 2018)       # object
print(book1.title)              # Når attributen direkt
print(book1.describe())         # Kallar metoden "describe" som retunerar alla 3 attribut.

class Bok:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def describe(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
bok1 = Bok("Ananas på Pizza", "Niclas Kempe", 2024)
print(bok1.title)
print(bok1.author)
print(bok1.year)

print(bok1.describe())
