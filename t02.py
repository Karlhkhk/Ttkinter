import tkinter as tk
import ctypes
from PIL import Image, ImageTk


def loe_fail(failinimi):
    with    open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()

def main():


        #Pilt
    aken = tk.Tk()
    aken.title("Mike Mentzer")
    aken.geometry("400x400")                             
    aken.resizable(False, True)
        # Label näide
    label = tk.Label(aken,
                     text="Mike Mentzer",
                     font=("Arial", 16, "bold"),
                     fg="black",
                     bg="navy blue",
                     padx=20,
                     pady=10)
    label.pack()

    # Pildi avamine ja Tkinteri jaoks ettevalmistamine
    pilt = Image.open("Mike_Mentzer.jpg")
    p = 20
    pilt = pilt.crop((0+p, 0+p, 200+p, 200+p))    
    foto = ImageTk.PhotoImage(pilt)

    # Pildi kuvamine Label abil
    label = tk.Label(aken, image=foto)
    label.image = foto  # Oluline: viide, et vältida garbage collectori poolt pildi kogemata kustutamist
    label.pack()


    
    #Tektsi kuvamine
    tekst = tk.Text(aken, wrap=tk.WORD)
    tekst.pack()
   
    failisisu = loe_fail("tekst.txt")
    tekst.insert(tk.INSERT, failisisu)
   
    #Kerimisriba
    tekst = tk.Text(aken, wrap=tk.WORD)
    # Kerimisriba loomine
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    # Kerimisriba positsiooni seadmine
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("tekst.txt")
    tekst.insert(tk.INSERT, failisisu)

    aken.mainloop()

if __name__ == "__main__":
    main()