import requests, argparse
from datetime import datetime
from threading import Thread, Lock
from queue import Queue

queue = Queue()
list_lock = Lock()
found_subdomains = []

def find(domain):

    global queue

    while True:

        subdomain = queue.get()
        url = f"https://{subdomain}.{domain}"

        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print(f"[*] {subdomain}\n\t\t{url}")
            print("- "*23)
            
            with list_lock:
                found_subdomains.append(url)

        queue.task_done()

def main(domain, threads, subdomains):
    
    global queue

    for subdomain in subdomains:
        queue.put(subdomain)

    for t in range(threads):
        worker = Thread(target=find, args=(domain,))
        worker.daemon = True
        worker.start()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Domain to check for subdomains")
    parser.add_argument("-w", "--wordlist", help="Wordlist to use for brute force")
    parser.add_argument("-t", "--threads", help="Number of threads to use to scan the domain", type=int, default=10)
    parser.add_argument("-o", "--output", nargs="?")

    args = parser.parse_args()

    domain = args.domain
    wordlist = args.wordlist
    threads = args.threads
    output_file = args.output

    print("\n" + "-"*45)
    print("Subdomain brute-force")
    print("Time started: " + str(datetime.now()))
    print("-"*45 + "\n")
    print("SUBDOMAIN      \tURL")
    print("-"*45)

    subdomains = open(wordlist).read().splitlines()

    try:
        main(domain, threads, subdomains)
        queue.join()

        if output_file:
            with open(output_file, "w") as f:
                for url in found_subdomains:
                    print(url, file=f)

    except KeyboardInterrupt:
        if output_file:
            with open(output_file, "w") as f:
                for url in found_subdomains:
                    print(url, file=f)
                    
        print("\nAborting subdomain brute-force...")