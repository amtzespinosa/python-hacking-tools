from scapy.all import ARP, Ether, srp
import sys

def arp_scan(target_ip):

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

def end():
    sys.exit()
