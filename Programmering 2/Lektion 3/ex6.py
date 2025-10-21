def divisionTal():
    while True:
        try:
            svar1 = float(input("Vänligen ange ett heltal: "))
            svar2 = float(input("Vänligen ange ett heltal att dividera med: "))
            resultat = svar1 / svar2
        except ValueError:
            print("Du har angett ett felaktigt värde. Vänligen ange ett heltal.")
        except ZeroDivisionError:
            print("0 är inte ett giltigt tal att använda i division. Vänligen försök igen.")
        except Exception as e:
            print("Något har gått fel.", e)
        else:
            print("Kvoten av", svar1, "och", svar2, "är: ", resultat)
        finally:
            print("Programmet är avslutat.")    
divisionTal()