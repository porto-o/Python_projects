# Made by: Ismael Porto ☺

import json
import tkinter as tk
from random import shuffle, randint, choice
from tkinter import messagebox
import pyperclip


# JSON operations in python
# write json.dump()
# read json.load()
# update json.update()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 6))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def confirm(website, username, password):
    confirm_text = f'website: {website}\n\nemail: {username}\n\npassword:{password}\n\nIs it correct?'
    confirmation = tk.messagebox.askyesno(title="Confirmation", message=confirm_text)
    return confirmation


def save_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if confirm(website, username, password):
        new_data = {
            website: {
                "email": username,
                "password": password
            }
        }

        if len(website) == 0 or len(username) == 0 or len(password) == 0:
            messagebox.showwarning(title="Error", message="Please do not leave any fields empty!")
        else:
            try:
                with open("passwords.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                tk.messagebox.showinfo(title="Success", message="Your information has been saved, your password is on "
                                                                "your clipboard!")
            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tk.messagebox.showerror(title="File not found", message="No Data File Found")
    else:
        if website in data:
            your_data = f'Your access for {website} is:\n\nemail: {data[website]["email"]}' \
                        f'\npassword: {data[website]["password"]}'
            tk.messagebox.showinfo(title="Your data", message=your_data)
        else:
            tk.messagebox.showinfo(title="ERROR", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password manager")

# labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = tk.Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = tk.Entry(width=30)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

username_entry = tk.Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
# username_entry.insert(tk.END, "ismael.porto2003@gmail.com")

password_entry = tk.Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
pass_btn = tk.Button(text="Generate Password", command=generate_password)
pass_btn.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=44, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tk.Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

# canvas
canvas = tk.Canvas(width=200, height=200)
photo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

with open("default_email.txt", "r") as f:
    default_email = f.read()
    username_entry.insert(tk.END, default_email)

window.resizable(False, False)
window.eval('tk::PlaceWindow . center')
window.mainloop()
