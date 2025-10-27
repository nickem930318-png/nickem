with open("kompisar1.txt") as file:
    line = file.read()
    names = line.strip().split(",")
    for name in names:
        print(f"Hej {name.strip()}, trevlig helg!")