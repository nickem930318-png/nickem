with open("kompisar.txt", "r") as file:
    for line in file:
        line = line.strip()
        print("Hej,", line, "Trevlig helg!")