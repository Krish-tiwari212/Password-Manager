import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
#----------------------------- SEARCH -------------------------------------------- #
def search():
    try:
        with open(r"data.json", mode="r") as data:
            new_data = json.load(data)
        web_site = new_data[web_entry.get()]
        pass_word = web_site["password"]
        email_data = web_site["email"]
        messagebox.showinfo(title=f"{web_entry.get()}", message=f"{email_data}\n{pass_word}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data found!")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="No data found!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
    new_data = {
        web: {
            "email": user,
            "password": passwrd
        }
    }
    if len(user) != 0 or len(passwrd) != 0:
        is_ok = messagebox.askokcancel(title="Are you sure?", message=f"Are you sure \n{user}\n{passwrd}\nIs correct?")
        if is_ok:
            try:
                with open(r"data.json", mode="r") as data:
                    new_data1 = json.load(data)
                    new_data1.update(new_data)

                with open(r"data.json", mode="w") as data:
                    json.dump(new_data1, data, indent=4)
                    password_entry.delete(0, END)
                    web_entry.delete(0, END)

            except json.JSONDecodeError:
                with open(r"data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)
                    password_entry.delete(0, END)
                    web_entry.delete(0, END)
            except FileNotFoundError:
                with open(r"data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)
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
web_entry = Entry(width=26)
web_entry.grid(row=1, column=1, sticky="W")
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2, sticky="W")
web_entry.focus()
username = Label(text="Email/Username:")
username.grid(row=2, column=0)
username_entry = Entry(width=46)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.focus()
username_entry.insert(0, "example@gmail.com")
password = Label(text="Password:")
password.grid(row=3, column=0)
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1, sticky="W")
password_entry.focus()
password_button = Button(text="Generate Password", command=pass_gen)
password_button.grid(row=3, column=2, sticky="W",)
add_button = Button(text="Add", width=39, command=save_password)
add_button.grid(row=5, column=1, columnspan=2)
window.mainloop()
