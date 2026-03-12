import random
import string
from tkinter import *

# Function to generate random password
def generate_password():
    # get length from user input
    try:
        length = int(entry_length.get())
    except:
        output_password.set("Enter a valid number")
        return

    # characters to use
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # create random password
    password = "".join(random.choice(all_chars) for _ in range(length))
    output_password.set(password)

# Function to copy password to clipboard using Tkinter
def copy_password():
    pwd = output_password.get()
    if pwd:
        root.clipboard_clear()        # clear old data
        root.clipboard_append(pwd)     # append new text
        root.update()                  # update clipboard immediately

# GUI Window
root = Tk()
root.title("Password Generator")
root.geometry("400x200")

# Label + input for length
Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)
entry_length = Entry(root, font=("Arial", 12))
entry_length.pack()

# Generate button
btn_generate = Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
btn_generate.pack(pady=10)

# Output field (generated password)
output_password = StringVar()
entry_password = Entry(root, textvariable=output_password, font=("Arial", 12), width=30)
entry_password.pack()

# Copy button
btn_copy = Button(root, text="Copy to Clipboard", command=copy_password, font=("Arial", 12))
btn_copy.pack(pady=10)

root.mainloop()