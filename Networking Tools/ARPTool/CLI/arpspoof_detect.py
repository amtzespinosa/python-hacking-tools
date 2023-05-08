from scapy.all import ARP, Ether, srp, sniff, conf
import sys

def get_mac(ip):

    ans, _ = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ip), timeout=3, verbose=0)

    if ans:
        return ans[0][1].src
    
def process(packet):

    if packet.haslayer(ARP):
        if packet[ARP].op == 2:
            try:
                real_mac = get_mac(packet[ARP].psrc)
                response_mac = packet[ARP].hwsrc

                if real_mac != response_mac:
                    print("[WARNING] You are under attack!")
                    print(f"Real MAC: {real_mac.upper()}.")
                    print(f"Fake MAC: {response_mac.upper()}.")

            except IndexError:
                pass

