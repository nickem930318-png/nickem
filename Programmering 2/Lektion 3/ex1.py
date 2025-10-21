def lasHeltal():
    try:
        heltal = int(input("Ange ett heltal: "))
        print("Du angav:", heltal)
    except:
        print("Felaktig inmatning. Ange endast heltal.")

lasHeltal()