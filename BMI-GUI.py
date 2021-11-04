import tkinter as tk

def functie(height, weight):
    Inaltime = int(height)
    Greutate = float(weight)
    Inaltime = Inaltime/100
    BMI = Greutate/(Inaltime*Inaltime)
    XX = str(BMI)

    Label1.destroy()
    Label2.destroy()
    tab1.destroy()
    tab2.destroy()
    buton.destroy()

    ran.config(text=f"Indexul tau este -->  {XX[:4]} \n")
    if BMI <= 16:
        rezultat.config(text=f"Risc major de boală", bg="red")
    elif BMI <= 18.5:
        rezultat.config(text=f"Risc minor de boală", bg="orange")
    elif BMI <= 25:
        rezultat.config(text=f"Sănătos", bg="green")
    elif BMI <= 30:
        rezultat.config(text=f"Supraponderal", bg="yellow")
    else:
        rezultat.config(text=f"Obezitate", bg="red")

def getEntry():
    text1 = tab1.get()
    text2 = tab2.get()
    functie(text1, text2)

Interfata = tk.Tk()
Interfata.config(bg="light blue")
Interfata.geometry("305x100")
Label1 = tk.Label(Interfata, text="Introdu înălțimea în centimetri:", bg="light blue")
tab1 = tk.Entry(Interfata, bg="light yellow")
Label2 = tk.Label(Interfata, text="Introdu greutatea în kilograme:", bg="light blue")
tab2 = tk.Entry(Interfata, bg="light yellow")
rezultat = tk.Label(Interfata, text="", bg="light blue")
buton = tk.Button(Interfata, text="Calculează", command=getEntry, bg="gray")
ran = tk.Label(Interfata, text="", bg="light blue")
Interfata.update()
Label1.grid(row=0, column=0)
tab1.grid(row=0, column=1)
Label2.grid(row=1, column=0)
tab2.grid(row=1, column=1)
rezultat.grid(row=3, column=2)
buton.grid(row=2, column=1)
ran.grid(row=2, column=2)

Interfata.mainloop()
