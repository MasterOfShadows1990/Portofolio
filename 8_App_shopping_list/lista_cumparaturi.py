# Gestiunea Listei de Cumpărături:

# Crează un program care să permită utilizatorului să adauge, să șteargă și să afișeze produsele dintr-o listă de cumpărături.
# Poți utiliza funcționalități precum adăugarea de produse, ștergerea produselor, afișarea listei curente, calcularea costului total al produselor, etc.
# Poți implementa această aplicație cu o interfață de linie de comandă sau poți utiliza o interfață grafică simplă.



import tkinter as tk
from tkinter import messagebox

# Lista de cumpărături
lista_cumparaturi = []

def afiseaza_lista():
    lista_text.config(state=tk.NORMAL)
    lista_text.delete(1.0, tk.END)
    if lista_cumparaturi:
        for index, produs in enumerate(lista_cumparaturi, start=1):
            lista_text.insert(tk.END, f"{index}. {produs}\n")
    else:
        lista_text.insert(tk.END, "Lista ta de cumpărături este goală.")
    lista_text.config(state=tk.DISABLED)

def adauga_produs():
    produs = produs_entry.get().strip()
    if produs:
        lista_cumparaturi.append(produs)
        afiseaza_lista()
        produs_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenție", "Te rog să introduci un produs.")

def curata_lista():
    lista_cumparaturi.clear()
    afiseaza_lista()

root = tk.Tk()
root.title("Lista de Cumpărături")
root.geometry("400x300")

titlu_label = tk.Label(root, text="Lista de Cumpărături", font=("Helvetica", 18))
titlu_label.pack(pady=10)

produs_frame = tk.Frame(root)
produs_frame.pack(pady=5)

produs_label = tk.Label(produs_frame, text="Introdu un produs:")
produs_label.grid(row=0, column=0, padx=5)

produs_entry = tk.Entry(produs_frame, width=30)
produs_entry.grid(row=0, column=1, padx=5)

adauga_button = tk.Button(produs_frame, text="Adaugă", command=adauga_produs)
adauga_button.grid(row=0, column=2, padx=5)

lista_frame = tk.Frame(root)
lista_frame.pack(pady=10)

lista_label = tk.Label(lista_frame, text="Lista ta de cumpărături:")
lista_label.grid(row=0, column=0, padx=5, sticky="w")

lista_text = tk.Text(lista_frame, height=8, width=40)
lista_text.grid(row=1, column=0, padx=5, pady=5)

scrollbar = tk.Scrollbar(lista_frame, command=lista_text.yview)
scrollbar.grid(row=1, column=1, sticky="nsew")
lista_text.config(yscrollcommand=scrollbar.set)

afiseaza_lista()

buton_frame = tk.Frame(root)
buton_frame.pack(pady=5)

curata_button = tk.Button(buton_frame, text="Curăță Lista", command=curata_lista)
curata_button.grid(row=0, column=0, padx=5)

inchide_button = tk.Button(buton_frame, text="Închide Aplicația", command=root.destroy)
inchide_button.grid(row=0, column=1, padx=5)

root.mainloop()























# lista_cumparaturi = []
# print("Bine ai venit la aplicatia ' Lista de cumparaturi'")
# user = input("Doresti sa intri in aplicatie?\n")
# if user != "da":
#     quit()
# while True:
#     produs = input("Introdu un produs:\n")
#     lista_cumparaturi.append(produs)

#     raspuns = input("Mai doresti sa adaugi ceva? (da/nu)\n")
#     if raspuns.lower() != 'da':
#         print(f"Lista ta de cumparaturi arata in felul urmator:{lista_cumparaturi}")
#         break



