import tkinter as tk
from tkinter import messagebox
import os

FILE_PATH = os.path.expanduser("~\\notes_wallpaper.txt")

def save_notes():
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", tk.END))

def load_notes():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return ""

root = tk.Tk()
root.title("Notes")
root.attributes("-fullscreen", True)  # Fullscreen
root.configure(bg="black")

text = tk.Text(root, bg="black", fg="white", insertbackground="white", font=("Consolas", 16), wrap=tk.WORD)
text.pack(fill=tk.BOTH, expand=True)
text.insert(tk.END, load_notes())

def on_close():
    save_notes()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
