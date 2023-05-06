# Python Hacking Tools Showcase 

These are some of the python tools and scripts I have crafted. I will be updating the repo as I code more or if any update needs to be made.

Some of them may have their own repo for further explanation/ease of installation (as in the case of the CLI tools).

## Index 
Groups and categories might not be the most correct ones. Any correction/suggestion is welcome!

- ### [Networking Tools](#networking-tools) 
  - **[Network Scanner](#network-scanner)**
  - **[ARPTool](#arp-tool)** - CLI Tool 
    - [ARP Scanner](#arp-scanner)
    - [ARP Spoofer](#arp-spoofer)
    - [ARP Spoofing detection](#arp-spoofer-detection)
  - **[Simple Port Scanner](#simple-scanner)**
  - **[Packet Sniffer](#packet-sniffer)**
  - **[DNS Spoofer](#dns-spoofer)**
  - **[FakeAP](#fakeap)** - Further features under development
  - **[Deauther](#deauther)** - Check [here](https://github.com/amtzespinosa/esp8266-wifi-deauther) the hardware version with an **ESP-8266** 
  
- ### [Remote Access](#remote-access)
  - **[Reverse Shell](#reverse-shell-client-side)** - Client side
  
- ### [Payloads](#payloads)
  - **[Keylogger](#keylogger)** - Includes .exe 
  - **[Reverse Shell](#reverse-shell-server-side)** - Server side 
  
- ### [Cryptography](#cryptography)
  - **[Dencrypter](#dencrypter)**
  
## Networking Tools
### Network Scanner
This is a simple airodump-ng like Network Scanner. To use it you will have to install some libs like Scapy (the base of almost all networking Python scripts) and Pandas for formatted output.

Use: 
'sudo python3 network_scanner.py -i wlan0'

You have to specify the NIC you are going to use and has to be in monitor mode.


