class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Initiera kontonumret som ett privat attribut
        self.__balance = initial_balance  # Initiera saldot som ett privat attribut

    # Getter-metod för att hämta kontonumret
    def get_account_number(self):
        return self.__account_number

    # Getter-metod för att hämta saldot
    def get_balance(self):
        return self.__balance

    # Setter-metod för att sätta nytt saldo, med kontroll så att saldot inte är negativt
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Ogiltigt saldo.")

    # Metod för att göra en insättning
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Lägg till beloppet till saldot
            print(f"Insatt {amount} kr på konto {self.__account_number}.")
        else:
            print("Ogiltigt insättningsbelopp.")

    # Metod för att göra ett uttag
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount  # Dra av beloppet från saldot
            print(f"Uttaget {amount} kr från konto {self.__account_number}.")
        else:
            print("Otillräckliga medel eller ogiltigt uttagsbelopp.")

    # Metod för att visa det aktuella saldot
    def display_balance(self):
        print(f"Kontonummer {self.__account_number} har saldot: {self.__balance} kr")

# Skapa en instans av BankAccount-klassen
account = BankAccount("123456789", 1000)

# Använd metoder för att göra insättningar, uttag och visa saldot
account.display_balance()  # Visa saldot
account.deposit(500)  # Gör en insättning
account.withdraw(200)  # Gör ett uttag
account.display_balance()  # Visa saldot igen
