import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, 'end')
    root.title("Untitled - Simple Text Editor")

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
        root.title(f"{file_path} - Simple Text Editor")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Save File", "File saved successfully!")

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# Menu Bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Text Area
text = tk.Text(root, wrap='word',font=("Helvetica", 12),undo=True,bg="light yellow",fg="black",padx=10,
                pady=10,borderwidth=2,  relief="groove"
              )           
  

text.pack(expand=True, fill='both')


scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side='right', fill='y')
text.config(yscrollcommand=scrollbar.set)

text.focus_set()

root.mainloop()
