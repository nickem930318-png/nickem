import os
if os.path.exists("c:\VSC\WP2\nickem\Programmering 2\Lektion 4\ny_mapp.txt"):
    os.remove("c:\VSC\WP2\nickem\Programmering 2\Lektion 4\ny_mapp.txt")
    print("Filen har tagits bort.")
else:
    print("Filen hittades inte.")
