#EXERCITIU FEED ME
#Trebuie sa creati o aplicatie GUI cu un singur buton.
#Cand aplicatia ruleaza,butonului i se atribuie un ascultator sau o comanda de evenimente click.



# https://dontpad.com/tamagoci

import tkinter as tk
from tkinter import messagebox
import random, time

class Window(tk.Tk):
    def __init__(self, title, square=400):
        super().__init__()
        self.title(title)
        self.geometry(f"{square}x{square}+{(self.winfo_screenwidth() - square)//2}+{(self.winfo_screenheight() - square)//2}")

        self.status_label = tk.Label(self,text="I am NOT hungry")
        self.status_label.pack()

        self.feed_button = tk.Button(self, text="Wait for it", command=lambda x=0: self.feed_tamagoci())
        self.feed_button.pack()
        self.is_game_ready = False


    def update_status(self):
        self.status_label.config(text="I am hungry!!!")
        self.feed_button.config(text="Feed me!!!")
        self.is_game_ready = True
        self.start_time = time.time()

    def feed_tamagoci(self):
        if self.is_game_ready == False:
            messagebox.showerror(title="Loser", message="De ce te grabesti?")
        else:
            reaction_time = time.time() - self.start_time
            messagebox.showinfo(title="Ai castigat", message=f"Ai reactionat in {reaction_time:.2f}")

    def start_game(self):
        self.wait_for_msec = random.randint(1, 5) * 1000
        print("start_game a fost chemat")
        print("trebuie sa asteptam:", self.wait_for_msec)
        self.status_label.after(self.wait_for_msec, lambda x=0: self.update_status())
    




if  __name__ == "__main__":
    window = Window("Tamagoci")
    window.start_game()
    window.mainloop()
    
    
