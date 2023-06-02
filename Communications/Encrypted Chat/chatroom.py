import socket, sys
from threading import Thread
from cryptography.fernet import Fernet

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator = "<SEP>"

client_sockets = set()
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen(5)
print(f"[*] Chat room opened at {SERVER_HOST}:{SERVER_PORT}")

def listen(clients):

    while True:
        try:
            message = clients.recv(10240).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(clients)
        else:
            message = message.replace(separator, ":")

        for client in client_sockets:
            client.send(message.encode())

if __name__ == "__main__":
    
    try:
        while True:
            client, client_addr = server.accept()
            print(f"[+] {client_addr} connected.")
            client_sockets.add(client)

            thread = Thread(target=listen, args=(client,))
            thread.daemon = True
            thread.start()

        if client_sockets:
            
            for client in client_sockets:
                client.close()

            server.close()
    
    except KeyboardInterrupt:
        
        server.close()
        sys.exit()