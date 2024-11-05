import tkinter as tk

window =tk.Tk()

square = 400
window.geometry(f"{square}x{square}+{(window.winfo_screenwidth() - square)//2}+{(window.winfo_screenheight() - square)//2}")




label = tk.Label(window,text="Textul de tradus")
label.pack()

input = tk.Entry(window)
input.pack()




VOCALE = "aeiou"
###VARINATA 1
def tradu_v1(text):
    pasa_text = ""
    for ch in text:
        if ch in VOCALE:
            pasa_text += (ch + "p" + ch)
        else:
            pasa_text += ch
    return pasa_text



###VARIANTA 2
def tradu_v2(text):
    for v in VOCALE:
        text = text.replace(f"{v}",f"{v}p{v}")
    return text




###VARINATA 3
def tradu(text):
   return "".join([ch if ch not in VOCALE else ch + "p" + ch for ch in text])




def pasareasca():
    text=input.get()

    label.config(text=tradu(text))

button = tk.Button(window,text="Tradu",command=pasareasca)
button.pack()

window.mainloop()