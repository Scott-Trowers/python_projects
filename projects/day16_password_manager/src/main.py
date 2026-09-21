import tkinter as tk
from tkinter import messagebox
import passman_funcs as pf
import pyperclip

LOGO_PATH = '../data/logo.png'
RAND_PW_LENGTH = 15

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    new_pw = pf.random_pw(RAND_PW_LENGTH)
    pass_ent.delete(0, tk.END)
    pass_ent.insert(0, string=new_pw)

    pyperclip.copy(new_pw)

# ----------------------------CLEAR INPUT ------------------------------ #
def clear_input():
    website_ent.delete(0, tk.END)
    email_username_ent.delete(0, tk.END)
    pass_ent.delete(0, tk.END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    details = {
        website_ent.get(): {
            "username": email_username_ent.get(),
            "password": pass_ent.get()
        }
    }

    first_key = next(iter(details))

    if first_key == '':
        succ_msg.set("Missing URL")
    elif details[first_key]["username"] == '':
        succ_msg.set("Missing username")
    elif details[first_key]["password"] == '':
        succ_msg.set("Missing password")
    else:
        succ_msg.set("Saved!")

        pf.update_details_file(details)

    clear_input()

    success_lab.config(text=succ_msg.get())

# ------------------------ SEARCH FOR DETAILS-------------------------- #
def search_details():
    website_to_search = website_ent.get()

    details = pf.search_details_file(website_to_search)

    if details is None:
        search_msg = f"No Details Found for:\n{website_to_search}"
    else:
        search_msg = f"Username: {details["username"]}\nPassword: {details["password"]}"

    clear_input()

    messagebox.showinfo(title="Password Search", message=search_msg)

# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title("PassMan")
window.config(
    width=320, height=320,
    padx=10, pady=10
)

# logo
bg_img = tk.PhotoImage(file=LOGO_PATH)
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)

# labels
website_lab = tk.Label(text="Website URL: ", highlightthickness=0, anchor='e')
website_lab.grid(column=0, row=1, sticky='e')

email_username_lab = tk.Label(text="Email/Username: ", highlightthickness=0, anchor='e')
email_username_lab.grid(column=0, row=2, sticky='e')

pass_lab = tk.Label(text="Password: ", highlightthickness=0, anchor='e')
pass_lab.grid(column=0, row=3, sticky='e')

succ_msg = tk.StringVar()
success_lab = tk.Label(text=succ_msg.get(), highlightthickness=0, fg='white')
success_lab.grid(column=2, row=4, sticky='w')

# entries
website_var = tk.StringVar()
website_ent = tk.Entry(background='white', fg='black', insertbackground='black')
website_ent.grid(column=1, row=1, sticky='ew')
website_ent.focus()

email_user_var = tk.StringVar()
email_username_ent = tk.Entry(background='white', fg='black', insertbackground='black')
email_username_ent.grid(column=1, row=2, columnspan=2, sticky='ew')

pass_var = tk.StringVar()
pass_ent = tk.Entry(background='white', show="*", fg='black', insertbackground='black')
pass_ent.grid(column=1, row=3, sticky='ew')

# buttons
search_but = tk.Button(text='Search', command=search_details)
search_but.grid(column=2, row=1, pady=(0, 4))

generate_but = tk.Button(text='Generate', command=generate_pw)
generate_but.grid(column=2, row=3, pady=(0, 4))

add_but = tk.Button(text='Save', command=save_details)
add_but.grid(column=1, row=4, pady=(0, 4))

window.mainloop()
