import _random
from tkinter import*
from tkinter import messagebox
import pyperclip
"""
Random password generator with a command-line search.
Based on user preferred characters and password length.
Character set handling. User input handling. GUI interface using PyQt. 
Allow users to copy password to clipboard for convenience. 
Enable users to customize password generation.
"""


root = Tk()
root.title("Random Password Generator")


# We want the user to create a password using one of these characters
uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!#$%&+="
numbers = "0123456789"
# We can use StrVar to ensure that the characters are random


#password = uppercase_characters + lowercase_characters + symbols + numbers
password_e = StringVar()
password_entry1 = Entry (root, textvariable = password_e,width = 40, border = 4)
password_entry1.pack()
password_entry1.get()


entrylabel = Label(root, text = "Please enter a password of 10 to 14 characters, including a number and symbol.")
entrylabel.pack(pady=10)

password_c = StringVar() # For added security measures, we have to ensure passwords match
password_entry2 = Entry (root, textvariable = password_c,width = 40, border = 4)
password_entry2.pack()
password_entry2.get()

confirmationlabel = Label (root, text = "Please confirm your password")
confirmationlabel.pack()

minimum_length = 8
maximum_length = 14

def passwordvalidation():
    if password_c.get() != password_e.get():
        messagebox.showerror("Error! Passwords do not match")
    if len(password_e.get()) < minimum_length:
       messagebox.showerror("Error!Password cannot be less than eight characters")
    if len(password_e.get()) > maximum_length:
       messagebox.showerror("Error!Password cannot be more than fourteen characters")
    else:
        messagebox.showinfo("Password Correct!")  

passwordbutton = Button(root, text = "Validate Password", command=passwordvalidation, bg="green") 
passwordbutton.pack(padx = 40, pady=20)



root.mainloop()