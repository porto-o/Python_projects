import tkinter as tk
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip


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
def save_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please dont leave any fields empty!")
    else:
        confirmation = messagebox.askokcancel(title=f'{website}',
                                              message=f'These are the details entered: \n\nEmail:{username} \nPassword:{password} \n\nIs it ok to save?')

        if confirmation:
            with open("Passwords.txt", "a") as f:
                f.write(f'{website} | {username} | {password} \n')
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
            messagebox.showinfo(title="Password Manager", message="Your data has been saved, the password is at your "
                                                                  "clipboard!")


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
website_entry = tk.Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

username_entry = tk.Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
username_entry.insert(tk.END, "ismael.porto2003@gmail.com")

password_entry = tk.Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
pass_btn = tk.Button(text="Generate Password", command=generate_password)
pass_btn.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=44, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

# canvas
canvas = tk.Canvas(width=200, height=200)
photo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

window.mainloop()
