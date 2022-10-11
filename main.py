from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def pass_gen():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_entry.delete(0, END)
    password_list = []
    password_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]
    password_list += symbol_list + number_list
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    user = username_entry.get()
    passwrd = password_entry.get()
    web = web_entry.get()
    if len(user) != 0 or len(passwrd) != 0:
        is_ok = messagebox.askokcancel(title="Are you sure?", message=f"Are you sure \n{user}\n{passwrd}\nIs correct?")
        if is_ok:
            with open(r"data.txt", mode="a") as data:
                data.write(f"{web} | {user} | {passwrd}\n")
                password_entry.delete(0, END)
                web_entry.delete(0, END)
    else:
        messagebox.showerror(title="Warning", message="Don't leave fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=30)
canvas = Canvas(height=200, width=160)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=image)
canvas.grid(row=0, column=1, sticky="W")
website = Label(text="Website:")
website.grid(row=1,column=0)
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
username = Label(text="Email/Username:")
username.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.focus()
username_entry.insert(0, "example@gmail.com")
password = Label(text="Password:")
password.grid(row=3, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, sticky="W")
password_entry.focus()
password_button = Button(text="Generate Password", command=pass_gen)
password_button.grid(row=3, column=1, sticky="E",columnspan=2)
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=5, column=1, columnspan=2)
window.mainloop()
