import tkinter as tk
from tkinter import filedialog
from pathlib import Path

import os

selected_files = []
def open_directory():
    directory
    DOCUMENTS_PATH = Path.home() / "Desktop"
    filename = filedialog.askopenfilename(
        initialdir=documents_path,
        filetypes=( 
                ("Pythoni failid", ("*.jpg", "*jpeg")),
                ("Kõik failid", "*.*")

        ),
        title
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
    else:
        dir_label.config(text="Kausta ei valitud.")


aken = tk.Tk()
aken.title("Validaator")
aken.geometry("400x300")


aken = tk.Tk()
aken.title("Pildi suuruse muutmine")
label = tk.Label(aken, text="Pildi suurus 200x200", font="Arial 24")
label.pack(pady=10)

open_button = tk.Button(aken, text="Ava kaust", command=open_directory)
open_button.pack(pady=10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)

aken.mainloop()