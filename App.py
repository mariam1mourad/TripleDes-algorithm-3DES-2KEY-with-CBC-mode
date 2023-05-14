from Crypto.Cipher import DES3
from hashlib import md5
from tkinter import *

def perform_operation():
    operation = operation_var.get()
    file_path = path_var.get()
    key = key_var.get()

    key_hash = md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()

        if operation == 'Encrypt':
            new_file_bytes = cipher.encrypt(file_bytes)
        else:
            new_file_bytes = cipher.decrypt(file_bytes)

    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)

# Create the form
root = Tk()
root.title("Encryption/Decryption Form")

# Operation input
operation_label = Label(root, text="Choose operation:")
operation_label.pack()
operation_var = StringVar(root)
operation_var.set("Encrypt")
operation_dropdown = OptionMenu(root, operation_var, "Encrypt", "Decrypt")
operation_dropdown.pack()

# File path input
path_label = Label(root, text="File path:")
path_label.pack()
path_var = StringVar(root)
path_entry = Entry(root, textvariable=path_var)
path_entry.pack()

# TDES key input
key_label = Label(root, text="TDES key:")
key_label.pack()
key_var = StringVar(root)
key_entry = Entry(root, textvariable=key_var)
key_entry.pack()

# Perform operation button
perform_button = Button(root, text="Perform Operation", command=perform_operation)
perform_button.pack()

# Start the form
root.mainloop()
