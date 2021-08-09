from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0, row=0)


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)

button.grid(column=1, row=1)

second_button = Button(text="Click me 2", command=action)
second_button.grid(column=2, row=0)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(column=3, row=3)

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(column=4, row=4)


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=5, row=5)


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=3, row=4)


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
window.mainloop()

# ================================================================================

# Advanced Arguments
# import turtle
# tim = turtle.Turtle()
# tim.write("hey")
#
# def add(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total
#
#
# print(add(1, 3, 5))


# def calculate(n, **kwargs):
#     for (key, value) in kwargs.items():
#         print(key)
#         print(value)
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(4, multiply=5, add=6)


# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")
#         self.seats = kwargs.setdefault("ns", 7)
#
#
# my_car = Car(make="Nissan")
# print(my_car.model)
# print(my_car.seats)
# my_car.seats = 8
# print(my_car.seats)
