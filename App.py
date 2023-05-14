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

