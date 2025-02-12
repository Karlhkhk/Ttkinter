import tkinter as tk
from tkinter import messagebox

# Loome peamise akna
aken = tk.Tk()
aken.title("Pitsapood")
aken.geometry("500x400")





# Loome muutujad, mis hoiavad märkeruutude olekuid
var1 = tk.IntVar()
var2 = tk.BooleanVar()

def show_selection():
    print(var1.get(), var2.get())
def show_selection():
    # print("Pitsa suurus:", selected_size.get())
    # print(var1.get(), var2.get(), var3.get())
    valikud = ["Kuller (+3€)", "Tulen ise järgi (0€)"]
    hinnad= [3,0]
    nr = valikud.index(selected_option.get())
    # print ("Valitud üksus:", hinnad[nr])
    Suurus = selected_size.get()
    Lisad = var1.get(), var2.get(), var3.get()
    Trans = hinnad[nr]
    Hind = Suurus+Lisad+Trans
    print (Hind)
    messagebox.showinfo("Pitsa hind", f"Tasumisele kuulub {Hind}")

tk.Label(aken, text="Kasutaja ID:", font="Arial 12").pack()
tk.Entry(aken).pack()
# Suuruse hind
selected_size = tk.IntVar(value=5)
tk.Label(aken, text="Vali pitsa suurus:", font="Arial 10").pack()

# Loome raadionupud
radio_red = tk.Radiobutton(aken, text="Väike (5€)", font="Arial 10", variable=selected_size, value=5)
radio_green = tk.Radiobutton(aken, text="Suur(8€)", font="Arial 10", variable=selected_size, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere(12€)", font="Arial 10", variable=selected_size, value=12)
radio_red.pack( )
radio_green.pack()
radio_blue.pack()


# Loome märkeruudud
tk.Label(aken, text="Vali pitsa lisandid:", font="Arial 10").pack()
var1 = tk.IntVar(value=0)
var2 = tk.DoubleVar(value=0.0)
var3 = tk.IntVar(value=0)



checkbox1 = tk.Checkbutton(aken, text="Juust(+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepporoni(+1,5€)", variable=var2, onvalue=1.5, offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="Seen(+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()
#dropdown valikud
valikud = ["Kuller(+3€)", "Tulen ise järgi(0€)"]
selected_option = tk.StringVar()
selected_option.set("Kuller (+3€)")
# Dropdown menüü loomine
dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()



def valik():

    print("Valitud üksus:", selected_option.get())

btn_confirm = tk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack(pady=(20, 0))
aken.mainloop()
