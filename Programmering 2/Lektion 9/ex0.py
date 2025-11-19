import tkinter as tk #Importerar bibliotek
def close_window(): #Definierar funktion för att stänga fönster
    root.destroy() # Huvudfönstret, som stänger applikationen

root=tk.Tk() # root är ett object av klassen Tk() som skapar huvudfönstret
root.title("Enkelt coolt fönster") # Sätter titeln på huvudfönstret.
# Skapar en knapp som anropar close_window när den klickas.
# Skapa en knappwidget med texten "Stäng fönster" och koppla den till funktionen

button  = tk.Button(root, text="Stäng fönster", command=close_window)
# Packa (placera) knappen i fönstret
button.pack(pady=80) # Packa (placera) knappen i fönstret med lite padding.
root.mainloop() # Startar huvudloopen för att köra applikationen
