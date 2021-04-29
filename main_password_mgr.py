from tkinter import *
import tkinter.messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ### Easy Solution ####
    no_letters = random.sample(letters, random.randint(4, 7))
    no_numbers = random.sample(numbers, random.randint(2, 5))
    no_symbols = random.sample(symbols, random.randint(2, 5))
    pass_selection = [no_letters, no_numbers, no_symbols]

    choice_pass = [choice for pword in pass_selection for choice in pword]
    shuffled = choice_pass
    random.shuffle(shuffled)
    choice_pass2 = ''.join(shuffled)
    password_enter.delete(0, END)
    password_enter.insert(0, choice_pass2)
    pyperclip.copy(choice_pass2)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    website = website_enter.get()
    email_user = email_user_enter.get()
    passwd = password_enter.get()
    # print(f'{website} | {email_user} | {passwd}')
    # if len(website) == 0 or len(email_user) == 0 or len(passwd):
    if not website or not email_user or not passwd:
        tkinter.messagebox.showwarning('Incomplete Information', 'Please fields are required.')
    else:
        is_ok = tkinter.messagebox.askokcancel(website,
                                               f'Details Entered: \nEmail/User: {email_user}\nPassword: {passwd}\nIs it okay to save??')
        if is_ok:
            with open('savepass.txt', 'a') as mypassmgr:
                mypassmgr.write(f'{website} | {email_user} | {passwd}\n')
            website_enter.delete(0, END)
            email_user_enter.delete(0, END)
            password_enter.delete(0, END)
            save_popup()


def save_popup():
    if save_pass:
        tkinter.messagebox.showinfo('Success', 'New Username and Password saved.')
    else:
        tkinter.messagebox.showerror('Failure', 'Something went wrong, Try Again.')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
# window.minsize(width=400, height=400)
window.config(padx=50, pady=50, bg='White')
image = PhotoImage(file='logo.png')

pass_canvas = Canvas(width=200, height=200, bg='White', highlightthickness=0)
pass_canvas.create_image(100, 100, image=image)
pass_canvas.grid(column=1, row=0)

# ------------------  Labels & Entries  ------------------------------- #

website_label = Label(text='Website', bg='white', fg='Black')
website_label.grid(column=0, row=1)

website_enter = Entry(width=50)
website_enter.grid(column=1, row=1, columnspan=2)
website_enter.focus()

###############################

email_user_label = Label(text='Email/Username', bg='white', fg='Black')
email_user_label.grid(column=0, row=2)

email_user_enter = Entry(width=50)
email_user_enter.grid(column=1, row=2, columnspan=2)
email_user_enter.insert(0, 'xyz@domain.com')

###############################

password_label = Label(text='Password', bg='white', fg='Black')
password_label.grid(column=0, row=3)

password_enter = Entry(width=32)
password_enter.grid(column=1, row=3)

#################################

generate_password = Button(text='Generate Password', bg='white', fg='Black', height=1, command=generate_passwd)
generate_password.grid(column=2, row=3)

#################################

add_button = Button(text='Add', bg='Light Blue', fg='Black', width=32, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
