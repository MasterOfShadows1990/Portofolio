# https://dontpad.com/tamagoci

import tkinter as tk
from tkinter import messagebox
import random, time


def update_status():
    global is_game_ready, start_time
    status_label.config(text="I am hungry!!!")
    feed_button.config(text="Feed me!!!")
    is_game_ready = True
    start_time = time.time()

def feed_tamagoci():
    global is_game_ready, start_time
    if is_game_ready == False:
        messagebox.showerror(title="Loser", message="De ce te grabesti?")
    else:
        reaction_time = time.time() - start_time
        messagebox.showinfo(title="Ai castigat", message=f"Ai reactionat in {reaction_time:.2f}")
    restart_game()


def restart_game():
    global is_game_ready 
    is_game_ready = False
    status_label.config(text="I am NOT hungry")
    feed_button.config(text="Wait for it")
    start_game()

def start_game():
    wait_for_msec = random.randint(1, 5) * 1000
    print("start_game a fost chemat")
    print("trebuie sa asteptam:", wait_for_msec)
    status_label.after(wait_for_msec, update_status)
    

window = tk.Tk()
window.title("Tamagoci")

is_game_ready = False
square = 400
window.geometry(f"{square}x{square}+{(window.winfo_screenwidth() - square)//2}+{(window.winfo_screenheight() - square)//2}")

status_label = tk.Label(window,text="I am NOT hungry")
status_label.pack()

feed_button = tk.Button(window, text="Wait for it", command=lambda x=0: feed_tamagoci())
feed_button.pack()

start_game()
window.mainloop()
    
    
