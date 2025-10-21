with open("C:/1namn.txt", "r") as file:
    line = file.read()
    nameList = line.strip().split(",")
    for names in nameList:
        names = names.strip()
        print(f"Hej, {nameList} ! Trevlig helg!")
