from scapy.all import ARP, Ether, srp
import argparse
from datetime import datetime

def arp_scan():

    arp = ARP(pdst=target_ip)
    ether = Ether(dst="FF:FF:FF:FF:FF:FF")
    packet = ether/arp
    result = srp(packet, timeout=3)[0]
    clients = []

    for sent, received in result:
        clients.append({"IP": received.psrc, "MAC": received.hwsrc})

    print("\nAvailable devices in the network:")
    print("\nIP" + " "*18 + "MAC\n")
    for client in clients:
        print("{:16}    {}".format(client["IP"], client["MAC"]))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Network IP address")

    args = parser.parse_args()

    target_ip = args.target

    print("\n" + "-"*45)
    print("Performing ARP Scan on: " + target_ip)
    print("Time started: " + str(datetime.now()))
    print("-"*45 + "\n")

    arp_scan()