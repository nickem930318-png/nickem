import os

sökväg = r"C:\kurs_projekt"
os.makedirs(sökväg, exist_ok=True)

filnamn = os.path.join(sökväg, "resultat.txt")

deltagare = ['Anna', 'Mohammed', 'Elina', 'Ali']

with open(filnamn, "w", encoding="utf-8") as fil:
    for namn in deltagare:
        rad = f"Namn: {namn}, Antal bokstäver: {len(namn)}\n"
        fil.write(rad)
print(f"Filen skapades i {filnamn}")




"""
nymapp = 'C:/kurs_projekt'
if not os.path.exists('C:/kurs_projekt'):
    os.mkdir('C:/kurs_projekt')
    print(f"Folder {nymapp} created.")
else:
    print(f"Folder {nymapp} already exists.")

nyfil = open("C:/kurs_projekt/resultat.txt", "w")

deltagare = ['Anna', 'Mohammed', 'Ali', 'Johan']

with open("C:/kurs_projekt/resultat.txt", "r") as file:
    for line in file:
"""