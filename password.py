from tkinter import BooleanVar
from random import choice, randint, shuffle
from string import ascii_letters, digits


class Password:

    def __init__(self):
        self.password = None
        self.passphrase = None

        self.letters = list(ascii_letters)
        self.numbers = list(digits)
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # default password not including numbers or symbols
        self.include_symbol = BooleanVar()
        self.include_numbers = BooleanVar()

        # sets default length for password/passphrase
        self.length = 8

        # read wordlist from text file and format words
        with open('wordlist.txt', 'r') as file:
            self.wordlist = [line.strip('\n').title() for line in file]

    def generate_password(self, field):
        """Generates random password containing letters/symbols/numbers (depending on if enabled)
         and assigns it to self.password; Updates UI"""

        empty_password = []

        # check whether to include symbols or numbers
        if self.include_symbol.get():
            empty_password += [choice(self.symbols) for _ in range(randint(1, 3))]

        if self.include_numbers.get():
            empty_password += [choice(self.numbers) for _ in range(randint(1, 5))]

        # add letters to password
        empty_password += [choice(self.letters) for _ in range(self.length)]

        # shuffle password
        shuffle(empty_password)

        # combine list and assign it
        self.password = "".join(empty_password)

        # call function to update UI with password
        self.update_entry(entry=field, string=self.password)

    def generate_passphrase(self, field):
        """Generate passphrase using random words from wordlist, assigns it to self.passphrase and updates UI"""
        passphrase_list = []

        for _ in range(self.length):
            passphrase_list.append(choice(self.wordlist))

        self.passphrase = "".join(passphrase_list)

        # call function to update UI with password
        self.update_entry(entry=field, string=self.passphrase)

    def update_entry(self, entry, string: str):
        """Clears any previous text from an entry then adds new text from string arg"""
        # clears any text in the field before inserting password
        entry.delete(first=0, last='end')

        # adds password to text entry
        entry.insert(index=0, string=string)

    def update_length(self, value):
        """sets the length of the password/phrase equal to position of slider in UI"""
        self.length = int(value)
