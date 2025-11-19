import tkinter as tk
from tkinter import messagebox # importerar messagebox/pop-up modulen
def popUp():
    svar = inmatning.get()
    messagebox.showinfo("Meddelande Pop", f"Du skrev: {svar}")


window = tk.Tk()
window.title("Inmatning och pop-up")
window.geometry("400x400")

inmatning = tk.Entry(window, width=40)
inmatning.pack(pady=15)
inmatning.focus() # placerar markören i objektet "inmatning"


button = tk.Button(window, text="Visa meddelande", command=popUp)
button.pack(pady=25)

window.mainloop()