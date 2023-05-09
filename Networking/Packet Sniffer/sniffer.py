from scapy.all import sniff, IP, Raw
from scapy.layers.http import HTTPRequest
import argparse
from datetime import datetime

def sniff_packets(iface=None):

    if iface:
        sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
    else:
        sniff(filter="port 80", prn=process_packet, store=False)

def process_packet(packet):

    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        ip = packet[IP].src
        method = packet[HTTPRequest].Method.decode()

        print(f"[+] {ip} requested {url} with {method}")

        if show_raw and packet.haslayer(Raw) and method == "POST":
            print(f"\n[*] Useful Raw data: {packet[Raw].load}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="Interface to use.")
    parser.add_argument("-r", "--show-raw", dest="show_raw", action="store_true", help="Show Raw data if any.")

    args = parser.parse_args()

    iface = args.interface
    show_raw = args.show_raw

    print("\n" + "-"*45)
    print("Packet sniffer running...")
    print("Time started: " + str(datetime.now()))
    print("-"*45 + "\n")

    sniff_packets()
