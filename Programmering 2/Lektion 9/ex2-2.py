import tkinter as tk

def increase_counter():
    current_value = int(label_counter['text'])
    label_counter.config(text=str(current_value + 1))

def decrease_counter():
    current_value = int(label_counter['text'])
    label_counter.config(text=str(current_value - 1))


window = tk.Tk()
window.title("Räkna med Kenny")
window.geometry("800x800")

label_counter = tk.Label(window, text="0")
label_counter.pack(pady=50)


increase_button = tk.Button(window, text="Increase", command=increase_counter)
increase_button.pack(side=tk.LEFT, padx=60)
                     
decrease_button = tk.Button(window, text="Decrease", command=decrease_counter)
decrease_button.pack(side=tk.RIGHT, padx=60)


window.mainloop()