from tkinter import *

window = Tk()
window.title(string="Miles to Km converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(column=10, row=0)

label_miles = Label()
label_miles.config(text="Miles")
label_miles.grid(column=11, row=0)

label = Label(text="is equal to")
label.grid(column=9, row=1)

label_result = Label(text="0")
label_result.grid(column=10, row=1)

label_km = Label(text="Km")
label_km.grid(column=11, row=1)


def calculate():
    answer = round((float(entry.get()) * 1.60934), 2)
    label_result.config(text=str(answer))


calculate_button = Button()
calculate_button.config(text="calculate", command=calculate)
calculate_button.grid(column=10, row=2)

window.mainloop()
