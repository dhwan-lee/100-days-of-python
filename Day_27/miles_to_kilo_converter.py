from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=10)

def calculate():
    mile = int(input.get())
    km = float(mile * 1.60934)
    label3.config(text=str(km))

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)
input.insert(END, string="0")

# Label
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()