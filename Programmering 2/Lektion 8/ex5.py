#Att rita en kvadrat med fylld färg.
# Den här övningen fungerar inte online. Kopiera koden och prova den i VS Code.
import turtle
t = turtle.Turtle()
t.color("green", "yellow")  # penfärg, fyllfärg
t.begin_fill()  # Börjar fylla formen med den angivna fyllfärgen (backgroundfärg).Fyllningen kommer inte att synas förrän man avslutar med "end_fill()".
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()  # Avslutar fyllningen och fyller den ritade formen med vald färg.
turtle.done()
