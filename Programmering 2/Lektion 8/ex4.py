#Rita en färgad triangel
# Den här övningen fungerar inte online. Kopiera koden och prova den i VS Code.
import turtle
t = turtle.Turtle() # Skapar ett turtle-objekt
t.pensize(3)  # Ställer in pennans tjocklek till 3 pixlar. pensize() används för att bestämma hur tjock linjen (strecket) ska vara när turtle ritar. 
t.color("blue")
for _ in range(3):
   t.forward(100)  # Flyttar framåt 100 pixlar och ritar en linje
   t.left(120)     # Svänger 120 grader åt vänster för att skapa en triangel
turtle.done()