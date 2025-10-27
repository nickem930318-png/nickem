counter = {
    "!" : 0,
    "@" : 0,
    "#" : 0,
} # dictionary för tecken vi vill räkna

with open("characters.txt", "r") as file: # öppna filen
    antalCharacters = file.read() # läs filen
    for x in antalCharacters: 
        try:
            counter[x] = counter[x] + 1 # +1 om tecknet finns i dictionary
        except:
            print("Character is not !, @, #.")

print(counter)