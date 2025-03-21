from tkinter import *
from datetime import datetime

def calculateAge():
    try:
        birthday = entry1.get()
        birthday = datetime.strptime(birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        label2.config(text=f"Your age is {age}")
    except ValueError:
        label2.config(text="Invalid input")

root = Tk()
root.title("Age Calculator")

label1 = Label(root, text="Enter your birthday:")
label1.pack(pady=10)

entry1= Entry(root)
entry1.pack(pady=10)

button1 = Button(root, text="Calculate Age", command=calculateAge)
button1.pack(pady=10)

label2 = Label(root)
label2.pack(pady=10)

root.mainloop()