#Rita flera cirklar med olika färger.
# Den här övningen fungerar inte online. Kopiera koden och prova den i VS Code.
import turtle
t = turtle.Turtle()
t.pensize(2)
färger = ["red", "blue", "green", "orange", "purple"]
radius = 30 # Startvärde för radien på den första cirkeln.
for färg in färger:
    t.color(färg)
    t.circle(radius)
    t.penup() # Lyfter pennan så att sköldpaddan kan flytta sig utan att rita på skärmen.
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown() # Sänker pennan så att sköldpaddan börjar rita igen när den rör sig.
    radius += 20 # Ökar värdet på variabeln radius med 20 varje gång det körs.
turtle.done()
