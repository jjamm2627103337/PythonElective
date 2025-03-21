from tkinter import *

def addition():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        sum = num1 + num2
        label3.config(text=f"Sum is: {sum}")
    except ValueError:
        label3.config(text="Invalid input")

root = Tk()
root.title("Addition")

label1 = Label(root, text="Enter first number: ")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(root, text="Enter second number: ")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

button1 = Button(root, text="Add", command=addition)
button1.grid(row=2, columnspan=2, padx=10, pady=10)

label3 = Label(root)
label3.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()