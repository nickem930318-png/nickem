# Den här övningen fungerar inte online. Kopiera koden och prova den i VS Code.
import turtle # turtle är namnet på biblioteket.
# Turtle() är en klass i biblioteket turtle som skapar ett objekt.
var = turtle.Turtle() # var är variabeln som håller objektet.
for _ in range(4): # att upprepa fyra gånger.
    var.forward(100) # Flytta framåt med 100 enheter.
    var.right(90) # Sväng höger 90 grader
# Avsluta ritningen
turtle.done() # Denna funktion håller fönstret öppet så att användaren kan se den ritade kvadraten innan programmet avslutas.
