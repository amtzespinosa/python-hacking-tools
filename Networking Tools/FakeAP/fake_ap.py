from scapy.all import RandMAC, sendp
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap

iface = "wlan0mon"
sender_mac = RandMAC()
ssid = "Test"
password = "1234"

dot11 = Dot11(type=0,subtype=8, addr1="FF:FF:FF:FF:FF:FF", addr2=sender_mac, addr3=sender_mac)
beacon = Dot11Beacon()
essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))

frame = RadioTap()/dot11/beacon/essid

print("-"*45)
print("FakeAP")
print("-"*45)
print("FakeAP Name:         " + ssid)
print("FakeAP Password:     " + password)
print("FakeAP MAC:          " + str(sender_mac))

sendp(frame, inter=0.1, iface=iface, loop=1)