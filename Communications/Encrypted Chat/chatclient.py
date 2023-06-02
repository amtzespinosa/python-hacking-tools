import socket, sys
from datetime import datetime
from threading import Thread
from cryptography.fernet import Fernet
#from chatroom import key

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002

client = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
client.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

key = "D8ZQNJVIyzpo74D-eGEVxHzFv9ZnU57UBM_eaERtE4U=".encode()
f_key = Fernet(key)

name = input("Enter a username: ")

def listen():
    
    while True:
        message = client.recv(10240)
        decrypted_message = f_key.decrypt(message)
        
        print("\n" + decrypted_message.decode())

if __name__ == "__main__":

    try:
        thread = Thread(target=listen)
        thread.daemon = True
        thread.start()

        while True:
            message = input()

            if message.lower() == "q":
                break

            message = f"[{str(datetime.now())}] {name}: {message}"
            message = message.encode()

            encrypted_message = f_key.encrypt(message)
            client.send(encrypted_message)

        client.close()

    except KeyboardInterrupt:

        client.close()
        sys.exit()
