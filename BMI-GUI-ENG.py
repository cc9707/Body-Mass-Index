import tkinter as tk

def function(height, weight):
    heighty = int(height)
    weighty = float(weight)
    heighty = heighty/100
    BMI = weighty/(heighty*heighty)
    XX = str(BMI)

    Label1.destroy()
    Label2.destroy()
    tab1.destroy()
    tab2.destroy()
    buton.destroy()

    ran.config(text=f"Your index is -->  {XX[:4]} \n")
    if BMI <= 16:
        result.config(text=f"Dangerously underweight", bg="red")
    elif BMI <= 18.5:
        result.config(text=f"Underweight", bg="orange")
    elif BMI <= 25:
        result.config(text=f"Healthy", bg="green")
    elif BMI <= 30:
        result.config(text=f"Overweight", bg="yellow")
    else:
        result.config(text=f"Obese", bg="red")

def getEntry():
    text1 = tab1.get()
    text2 = tab2.get()
    function(text1, text2)

Interface = tk.Tk()
Interface.config(bg="light blue")
Interface.geometry("305x100")
Label1 = tk.Label(Interface, text="Add your height in centimeters:", bg="light blue")
tab1 = tk.Entry(Interface, bg="light yellow")
Label2 = tk.Label(Interface, text="Add your weight in kilograms:", bg="light blue")
tab2 = tk.Entry(Interface, bg="light yellow")
result = tk.Label(Interface, text="", bg="light blue")
buton = tk.Button(Interface, text="Calculate", command=getEntry, bg="gray")
ran = tk.Label(Interface, text="", bg="light blue")
Interface.update()
Label1.grid(row=0, column=0)
tab1.grid(row=0, column=1)
Label2.grid(row=1, column=0)
tab2.grid(row=1, column=1)
result.grid(row=3, column=2)
buton.grid(row=2, column=1)
ran.grid(row=2, column=2)

Interface.mainloop()
