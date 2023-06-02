import subprocess, string, random, re, argparse
from datetime import datetime

def random_mac():

    upper_hex = "".join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(upper_hex)
        mac += ":"
    return mac.strip(":")

def get_mac(iface):
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def change_mac(iface, new_mac):
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac}", shell=True)
    subprocess.check_output(f"ifconfig {iface} up", shell=True)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="Network interface")
    parser.add_argument("-r", "--random", action="store_true", help="Generates random MAC address")
    parser.add_argument("-m", "--mac", help="New MAC to change to")

    args = parser.parse_args()

    iface = args.interface

    if args.random:
        new_mac = random_mac()
    elif args.mac:
        new_mac = args.mac
    
    old_mac = get_mac(iface)

    print("\n" + "-"*45)
    print("Changing MAC address for: ", iface)
    print("Time started: " + str(datetime.now()))
    print("-"*45 + "\n")

    print("[*] Old MAC address: ", old_mac)
    change_mac(iface, new_mac)
    new_mac = get_mac(iface)
    print("[*] New MAC address: ", new_mac)
