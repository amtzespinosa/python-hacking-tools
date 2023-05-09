from scapy.layers.dot11 import Dot11, Dot11Elt, Dot11Beacon, sniff
from threading import Thread
import time, os, pandas, argparse

networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm", "CH", "SECURITY"])
networks.set_index("BSSID", inplace=True)

def callback(packet):

    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()

        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"

        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        security = stats.get("crypto")

        networks.loc[bssid] = (ssid, dbm_signal, channel, security)

def change_channel():

    ch = 1
    while True:
        os.system(f"sudo iwconfig {interface} channel {ch}")
        ch = ch % 14 + 1
        time.sleep(0.5)

def print_all():
    while True:
        os.system("clear")
        print(networks)
        time.sleep(0.5)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="Network interface in Monitor mode")

    args = parser.parse_args()

    interface = args.interface

    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()

    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()

    sniff(prn=callback, iface=interface)

