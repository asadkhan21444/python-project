import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
label = tk.Label(root, font=("Halvetica", 48), bg="black",fg="cyan")
label.pack(anchor="center")

def update_clock():
    now = datetime.now().strftime("%H:%M:%S:%p")
    label.config(text=now)
label.after(1000, update_clock)
update_clock()
root.mainloop()