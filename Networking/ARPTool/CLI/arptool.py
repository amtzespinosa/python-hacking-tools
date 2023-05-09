import argparse, sys, time, arpscan, arpspoof, arpspoof_detect
from datetime import datetime

if __name__ == "__main__":

    if sys.argv[1] == "-s" or sys.argv[1] == "--scan":

        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--scan", help="Network IP address")

        args = parser.parse_args()

        target_ip = args.scan

        print("\n" + "-"*45)
        print("Performing ARP Scan on: " + target_ip)
        print("Time started: " + str(datetime.now()))
        print("-"*45 + "\n")

        arpscan.arp_scan(target_ip)

        sys.exit()
        
    else:
        pass

    if (sys.argv[1] == "-t" or sys.argv[1] == "--target") and (sys.argv[3] == "-g" or sys.argv[3] == "--gateway"):

        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", help="Target IP address")
        parser.add_argument("-g", "--gateway", help="Gateway IP address")
        parser.add_argument("-v", "--verbose", action="store_true", help="Default: True")

        args = parser.parse_args()

        target = args.target
        host = args.gateway
        verbose = args.verbose

        verbose=True

        print("\n" + "-"*45)
        print("Performing ARP Spoofing attack on: " + target)
        print("Time started: " + str(datetime.now()))
        print("-"*45 + "\n")

        arpspoof.enable_ip_route()

        try:
            while True:
                arpspoof.arp_spoof(target, host, verbose)
                arpspoof.arp_spoof(host, target, verbose)
                time.sleep(1)

        except KeyboardInterrupt:
            print("\n[!] Restoring the network... Please wait.")
            arpspoof.restore(target, host)
            arpspoof.restore(host, target)
            arpspoof.disable_ip_route()
        
        sys.exit()
        
    else:
        pass

    if sys.argv[1] == "-d" or sys.argv[1] == "--detect":

        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--detect", help="Perform ARP Spoof detection")

        args = parser.parse_args()

        iface = args.detect

        print("\n" + "-"*45)
        print("ARP Spoof detection running...")
        print("Time started: " + str(datetime.now()))
        print("-"*45 + "\n")

        arpspoof_detect.sniff(store=False, prn=arpspoof_detect.process)
    
    else:
        sys.exit()
 
