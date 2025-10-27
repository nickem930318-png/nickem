"""
fil = open(r"c:\VSC\WP2\nickem\Programmering 2\Lektion 4\ex6.txt", "a")
fil.write("Text1")
fil.close

fil = open(r"c:\VSC\WP2\nickem\Programmering 2\Lektion 4\ex6.txt", "r")
print(fil.read())
fil.close

fil = open(r"c:\VSC\WP2\nickem\Programmering 2\Lektion 4\ex6.txt", "a")
fil.write("Lite mer text.")
fil.close
"""

with open("xmpl6.txt", "w") as fil:
    fil.write("This is some content to the .txt-file. ")

with open("xmpl6.txt", "r") as fil:
    innehall = fil.read()
    print("Innehållet i filen är:", innehall)

with open("xmpl6.txt", "a") as fil:
    fil.write("Detta läggs till i slutet av filen genom append.")

with open("xmpl6.txt", "r") as fil:
    innehall = fil.read()
    print("Uppdaterat innehåll:", innehall)