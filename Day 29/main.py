import json
from tkinter import messagebox
from tkinter import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import randint, choice, shuffle


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(text=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# website label
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

# website entry
website_entry = Entry()
website_entry.config(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# email label
email_username_label = Label()
email_username_label.config(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# email entry
email_username_entry = Entry()
email_username_entry.config(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, string="danielabraha99@gmail.com")

# password label
password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

# password entry
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)



# generate password button
generate_password_button = Button()
generate_password_button.config(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)





def save_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("login.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("login.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# add button
add_button = Button()
add_button.config(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


def search_data():
    website = website_entry.get()
    try:
        with open("login.json", mode="r") as file:
            info = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Not data file found")
    else:
        if website in info:
            email = info[website]["email"]
            password = info[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


search_button = Button()
search_button.config(text="Search", command=search_data)
search_button.grid(column=2, row=1)

window.mainloop()
