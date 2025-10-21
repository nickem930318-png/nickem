
def kvadreraTal():
    try:
        tal = int(input("Vänligen ange ett heltal att kvadrera: "))
        print(pow(tal, 2))
    except Exception as e:
        print("Felaktig input.", e)

kvadreraTal()