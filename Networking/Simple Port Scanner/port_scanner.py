import socket, argparse, sys
from datetime import datetime
from threading import Thread
from queue import Queue

N_THREADS = 200
queue = Queue()
    
def port_scan(port):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #socket.setdefaulttimeout(10)
    result = client.connect_ex((host, port))

    if result == 0:
        print(host + " "*5 + "Port {} is open".format(port))
        client.close()

def port_scan_thread():

    global queue

    while True:
        worker = queue.get()
        port_scan(worker)
        queue.task_done()

def scan(host, ports):

    global queue

    for thread in range(N_THREADS):
        thread = Thread(target=port_scan_thread)
        thread.daemon = True
        thread.start()

    for worker in ports:
        queue.put(worker)

    queue.join()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="Target host IP address")
    parser.add_argument("-p", "--ports", dest="port_range", help="Target ports to scan")

    args = parser.parse_args()

    host = args.host

    port_range = args.port_range
    
    start_port, end_port = port_range.split(",")
    start_port, end_port = int(start_port), int(end_port)

    print("Scanning host: " + host)
    print("Time started: " + str(datetime.now()) + "\n")

    try:
        ports = [port for port in range(start_port, end_port)]
        
        scan(host, ports)
    
    except KeyboardInterrupt:
        print("\nExiting Program...")
        sys.exit()
    except socket.gaierror:
        print("Host name could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()



