from password import Password
from tkinter import *
from tkinter import messagebox

ui = Tk()
password = Password()

# setting up ui information
ui.title('Password Generator')
ui.geometry('550x500')
ui.iconbitmap('lock-1332-475024.ico')
ui.config(pady=50, padx=50)

# logo
img = PhotoImage(file='lock-1332-475024.png')
image = Label(ui, image=img)

# entry
textfield = Entry(ui)
textfield.config(width=40)

# button and messagebox explaining passphrases
explain = Button(ui,
                 text='Why?',
                 fg='blue',
                 bd=0,
                 command=lambda: messagebox.showinfo(
                     title='Passphrases',
                     message='Passphrases are an easy to remember but harder to crack alternative to passwords,'\
                             'They typically range from 16-100 characters.\n\n'\
                             'More info/source: https://www.techtarget.com/searchsecurity/definition/passphrase'
                 ))

# password/phrase buttons
pw_button = Button(ui, text="Generate Password", command=lambda: password.generate_password(field=textfield), width=17)
ps_button = Button(ui, text="Generate Passphrase", command=lambda: password.generate_passphrase(field=textfield),
                   width=17)

# checkboxes for numbers and symbols in password
numbers = Checkbutton(ui, text="Numbers", variable=password.include_numbers, onvalue=True, offvalue=False)
symbols = Checkbutton(ui, text="Symbols", variable=password.include_symbol, onvalue=True, offvalue=False)

# slider for password/passphrase length
length = Scale(ui, orient=HORIZONTAL, from_=5, to=16, variable=password.length, command=password.update_length)

# Styling
image.grid(column=1, row=0)
textfield.grid(column=1, row=1, rowspan=2)

numbers.grid(column=0, row=1, padx=10)
symbols.grid(column=0, row=2, padx=10)

pw_button.grid(column=2, row=1)
ps_button.grid(column=2, row=2)

length.grid(column=1, row=3)
length.set(value=8)

explain.grid(column=2, row=3)

# Runs the UI
ui.mainloop()
