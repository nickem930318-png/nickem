file = open(r"c:\VSC\WP2\nickem\Programmering 2\Lektion 4\ny_mapp.txt", "a")
file.write("I like Python")
file.close()

file = open(r"c:\VSC\WP2\nickem\Programmering 2\Lektion 4\ny_mapp.txt", "r")
print(file.read())
file.close()