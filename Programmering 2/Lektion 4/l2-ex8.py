import os
deltagare = ['Kenny', 'Benny', 'Jenny']

if not os.path.exists("Programmering 2\Lektion 4\EX8"):
    os.makedirs("Programmering 2\Lektion 4\EX8")

with open ("Programmering 2\Lektion 4\EX8\my_friends.txt", "w") as fil:
    for y in deltagare:
        fil.write(f"Hej {y}!\n")
