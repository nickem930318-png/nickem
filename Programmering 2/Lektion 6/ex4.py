class Student:
    def __init__(self, name, age, grade):
        # Privata attribut för att skydda elevens data
        self.__name = name
        self.__age = age
        self.__grade = grade

    # Metod för att hämta elevens namn
    def get_name(self):
        return self.__name  # Returnerar det privata attributet __name

    # Metod för att hämta elevens ålder
    def get_age(self):
        return self.__age  # Returnerar det privata attributet __age

    # Metod för att hämta elevens betyg
    def get_grade(self):
        return self.__grade  # Returnerar det privata attributet __grade

 

    # Metod för att ändra elevens ålder
    def set_age(self, age):
        self.__age = age  # Uppdaterar det privata attributet __age med ett nytt värde


    # Metod för att visa elevens information
    def show_info(self):
        # Skriv ut elevens namn, ålder och betyg
        print(f"Name: {self.__name}")  # Visar elevens namn
        print(f"Age: {self.__age}")    # Visar elevens ålder
        print(f"Grade: {self.__grade}")  # Visar elevens betyg

# Skapa en instans av Student-klassen med namn, ålder och betyg
student1 = Student("Anna Svensson", 15, "A")

# Anropa metoden för att visa information om eleven
student1.show_info()

# Använd set-metoder för att ändra elevens ålder
student1.set_age(16)   # Ändra åldern till 16
#student1.set_name("Samer")   #Du får inte ändra namnet.
# student1.set_grade("B") #Du får inte ändra betyget

# Skriv ut en rubrik för uppdaterad information
print("\nUpdated Student Information:")

# Visa den uppdaterade informationen om eleven
student1.show_info()