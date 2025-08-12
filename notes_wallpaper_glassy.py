import tkinter as tk
import os

# Path to store notes
FILE_PATH = os.path.expanduser("~\\notes_wallpaper.txt")

# Save notes to file
def save_notes():
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", tk.END))

# Load notes from file
def load_notes():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Create main window
root = tk.Tk()
root.title("Wallpaper Notes")
root.geometry("800x500")
root.configure(bg="black")

# Add close & minimize buttons by not using fullscreen
root.overrideredirect(False)

# Glassy transparent effect (alpha < 1)
root.attributes('-alpha', 0.88)

# Text widget for note entry
text = tk.Text(
    root,
    bg="#1c1c1c",             # dark gray background
    fg="white",               # white text
    insertbackground="white", # white cursor
    font=("Consolas", 14),
    wrap=tk.WORD,
    relief=tk.FLAT,
    borderwidth=10
)
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Load existing notes
text.insert(tk.END, load_notes())

# Save notes when window is closed
def on_close():
    save_notes()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# Start the app
root.mainloop()
