def gissaNummer(hemligaNumret, gissning):
    if gissning == hemligaNumret:
        return True
    elif gissning < hemligaNumret:
        print("För lågt! Gissa högre dummer!")
    else:
        print("För högt! Gissa lägre dummer!")
    return False

hemligaNumret = 7

gissat_ratt = False
antal_gissningar = 0
while not gissat_ratt:
    antal_gissningar += 1
    gissning = int(input(f"Gissning nr {antal_gissningar}: "))
    gissat_ratt = gissaNummer(hemligaNumret, gissning)

print(f"Grattis, du gissade rätt på {antal_gissningar} försök!")