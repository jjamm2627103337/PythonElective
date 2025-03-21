from tkinter import *

def toCelcius():
    f = float(entry1.get())
    c = (f - 32) * 5 / 9
    entry2.delete(0,END)
    entry2.insert(0, f"{c}")
    
def toFahrenheit():
    c = float(entry2.get())
    f = c * 9 /5 +32
    entry1.delete(0,END)
    entry1.insert(0, f"{f}")

root = Tk()
root.title("Converter")

label1 = Label(root, text="Temperature in Fahrenheit:")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = Label(root, text="Temperature in Celcius:")
label2.grid(row=0, column=1, padx=10, pady=10)

entry1 = Entry(root)
entry1.grid(row=1, column=0, padx=10, pady=10)
entry1.insert(0, "32.00")

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry2.insert(0, "0.00")

button1 = Button(root, text=">>>>", command=toCelcius)
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = Button(root, text="<<<<", command=toFahrenheit)
button2.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()




