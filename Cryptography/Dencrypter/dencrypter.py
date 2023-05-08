from cryptography.fernet import Fernet
import argparse, sys
from os.path import exists
import os

def generate_new_key():

        key = Fernet.generate_key()
        with open(key_filename, "wb") as key_file:
            key_file.write(key)

def load_key():

    return open(key_filename, "rb").read()

def encrypt_file(filename, key):

    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):

    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":

    if sys.argv[1] == "-g" or sys.argv[1] == "--generate":

        parser = argparse.ArgumentParser()
        parser.add_argument("-g", "--generate", help="Generate new Key File")

        args = parser.parse_args()

        key_filename = args.generate

        if not exists(key_filename):
            generate_new_key()
            print("Key generated succesfully at " + os.getcwd() + key_filename)
        else:
            print("Key file already exists.")

    if sys.argv[1] == "-e" or sys.argv[1] == "--encrypt":

        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--encrypt", help="Filename to encrypt")
        parser.add_argument("-k", "--key", help="Key filename to encrypt")

        args = parser.parse_args()

        file = args.encrypt
        key_filename = args.key
        key = load_key()

        encrypt_file(file, key)
        print("The file [" + file + "] has been successfully encrypted using [" + key_filename + "].")

    else:
        pass

    if sys.argv[1] == "-d" or sys.argv[1] == "--decrypt":

        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--decrypt", help="Filename to decrypt")
        parser.add_argument("-k", "--key", help="Key filename to decrypt")

        args = parser.parse_args()

        file = args.decrypt
        key_filename = args.key
        key = load_key()

        decrypt_file(file, key)
        print("The file [" + file + "] has been successfully decrypted using [" + key_filename + "].")