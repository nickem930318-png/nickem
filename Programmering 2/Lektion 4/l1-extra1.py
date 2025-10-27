"""
def matematik():
    svar1 = int(input("Vänligen inkom med det första heltalet: "))
    svar2 = int(input("Vänligen inkom med det andra heltalet: "))
    print("Dessa tal kommer nu användas i addition, subtraktion, multiplikation och division nedan.")
    print(f"Addition: Summan av {svar1} och {svar2} är {svar1 + svar2}.")
    print(f"Subtraktion: Differensen av {svar1} och {svar2} är {svar1 - svar2}.")
    print(f"Multiplikation: Produkten av {svar1} och {svar2} är {svar1 * svar2}.")
    print(f"Division: Kvoten av {svar1} och {svar2} är {svar1 / svar2}.")

matematik() """

def addition(x, y):
    return x + y
def subtraktion(x, y):
    return x - y
def division(x, y):
    if y == 0:
        return ("Error: Can't divide by zero.")
    else:
        return x / y
def multiplikation(x, y):
    return x * y

print("1. Addition")
print("2. Subtraktion")
print("3. Muliplikation")
print("4. Division")

while True:
    val = input("Välj ett nummer mellan 1-4: ")
    if val in ("1", "2", "3", "4"):
        firstnumber = int(input("Ange det första talet: "))
        secondnumber = int(input("Ange det andra talet: "))
    if val == "1":
        print(f"Summan av {firstnumber} och {secondnumber} är {addition(firstnumber, secondnumber)}")
    if val == "2":
        print(f"Differensen av {firstnumber} och {secondnumber} är {subtraktion(firstnumber, secondnumber)}.")
    if val == "3":
        print(f"Produkten av {firstnumber} och {secondnumber} är {multiplikation(firstnumber, secondnumber)}.")
    if val == "4":
        print(f"Kvoten av {firstnumber} och {secondnumber} är {division(firstnumber, secondnumber)}")
    next_calculation = input("Vill du räkna ut nästa tal? (J/N): ")
    if next_calculation.upper() == "N":
       break
