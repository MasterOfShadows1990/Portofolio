import tkinter as tk 
from tkinter import messagebox

window = tk.Tk()
# square = 400
# window.geometry(f"{square}x{square}+{(window.winfo_screenwidth() -square)//2}+{(window.winfo_screenheight() -square)//2}")


def saluta():
    nume = input.get()
    if nume:
        messagebox.showinfo(title="Salutare",message=f"Salut,{nume}!")
    else:
        messagebox.showinfo(title="Salutare",message=f"Te rog sa te prezinti!")

label = tk.Label(window,text="Intro numele")
label.pack()


input = tk.Entry(window)
input.pack()


button = tk.Button(window,text="Saluta",command=saluta)
button.pack()
# button.configure()


window.mainloop()