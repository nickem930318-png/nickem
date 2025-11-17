class Person:
    # Konstruktor för Person-klassen, tar förnamn och efternamn som argument.
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    
# Definierar subklassen Student som ärver från Person.
class Student(Person):
    # Konstruktor för Student-klassen, tar förnamn, efternamn och ålder som argument.
    def __init__(self, fname, lname, ålder):
        super().__init__(fname, lname)  # Anropar basklassens konstruktor för att initiera firstname och lastname.
        self.ålder = ålder
    
    # Ny metod för att skriva ut studentens fullständiga namn och ålder.
    def printname(self):
        print(f"Namn: {self.firstname} {self.lastname}, Ålder: {self.ålder}")

# Skapa ett Student-objekt och skriv ut dess information.
x = Student("Mike", "Olsen", 35)
x.printname()