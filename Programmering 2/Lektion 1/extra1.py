def medellonprog(loner): # Beräkna medellön från lista
    antal_loner = len(loner)
    if antal_loner == 0:
        return None # Ingen lön
    medellon = sum(loner) / antal_loner
    return medellon

# Hämta antal löner
antal_loner = int(input("Ange antalet löner att mata in: "))

# List för löner
loner = []

# Loop för att hämta olika löner
for i in range(antal_loner):
  #"f" är en prefix för en så kallad "f-string" i Python. Den tillåter dig att inkludera variabler direkt inuti en sträng genom att placera dem inom klammerparentes {}.
  lon = float(input(f"Ange lön nr {i+1}: "))
  loner.append(lon)

# Beräkna medel lön
medellon = medellonprog(loner)

# Visa resultat
print("Medel lönen är:", medellon)