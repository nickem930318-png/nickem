def beraknaMedellon(loner):
    antalLoner = len(loner)
    if antalLoner == 0:
        return None
    medellon = sum(loner) / antalLoner
    return medellon

antalLoner = int(input("Ange antalet löner att mata in: "))

loner = []

for i in range(antalLoner):
    lon = float(input(f"Ange lön nr {i+1}: "))
    loner.append(lon)

medellon = beraknaMedellon(loner)

print("Medel lönen är:", medellon)