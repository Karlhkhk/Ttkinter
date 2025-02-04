import tkinter as tk
import ctypes

def main():
    # DPI teadlikkuse seadistamine kõrge DPI ekraanide jaoks
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception as e:
        print(e)

    aken = tk.Tk()
    aken.title("Karli Tkinter")
    aken.geometry("400x300")
   
    label = tk.Label(aken, text="Ma vihkan neegreid").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()