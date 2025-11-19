import tkinter as tkalias #tkalias kan vara vad som helst, preferensen är att ha något som är enkelt att skriva
def changeLabelText():
    label.config(text="Bananchoklad")

window =tkalias.Tk()
window.title("Ändra till bananchokladen")

label = tkalias.Label(window, text="Mangopaj")
label.pack()

button = tkalias.Button(window, text="Tryck för att ändra!", command=changeLabelText)
button.pack()

window.mainloop()