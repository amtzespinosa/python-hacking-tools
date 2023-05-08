from scapy.all import ARP, Ether, srp, sniff, conf
import sys

def get_mac(ip):

    # Returns MAC addr if IP is up
    ans, _ = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ip), timeout=3, verbose=0)

    if ans:
        return ans[0][1].src
    
def process(packet):

    # Is the packet an ARP packet?
    if packet.haslayer(ARP):
        # If it is ARP response
        if packet[ARP].op == 2:
            try:
                # Get real MAC addr
                real_mac = get_mac(packet[ARP].psrc)

                # Get the MAC addr from packet sent to us
                response_mac = packet[ARP].hwsrc

                # Not equal = we're under attack!
                if real_mac != response_mac:
                    print("[WARNING] You are under attack!")
                    print(f"Real MAC: {real_mac.upper()}.")
                    print(f"Fake MAC: {response_mac.upper()}.")

            except IndexError:
                # Unable to find real MAC
                pass

if __name__ == "__main__":

    try:
        iface = sys.argv[1]
    except:
        iface = conf.iface

    sniff(store=False, prn=process)

