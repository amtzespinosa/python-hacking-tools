# Python Hacking Tools Showcase 

These are some of the python tools and scripts I have crafted so far. I will be updating the repo as I code more or if any update needs to be made.

Some of them may have their own repo for further explanation/ease of installation (as in the case of the CLI tools).

> **Note:** I know many of the scripts are not precisely clean neither efficient. This is because they were coded in a rush during some jobs and fastly and poorly cleaned afterwards. My apologies.

## Index 
Groups and categories might not be the most correct ones. Any correction/suggestion is welcome!

- **[Networking](#networking)** 
  - [Network Scanner](#network-scanner)
  - [ARPTool](#arp-tool) *- CLI Tool + individual scripts* 
    - *[ARP Scanner](#arp-scanner)*
    - *[ARP Spoofer](#arp-spoofer)*
    - *[ARP Spoofing detection](#arp-spoofer-detection)*
  - [Simple Port Scanner](#simple-port-scanner)
  - [Packet Sniffer](#packet-sniffer)
  - [DNS Spoofer](#dns-spoofer)
  - [FakeAP](#fakeap) *- Further features under development*
  - [Deauther](#deauther) *- Check [here](https://github.com/amtzespinosa/esp8266-wifi-deauther) the hardware version with an **ESP-8266*** 
  
- **[Remote Access](#remote-access)**
  - [Reverse Shell](#reverse-shell-client-side) *- Client side*
  
- **[Payloads](#payloads)**
  - [Keylogger](#keylogger) *- Includes **.exe*** 
  - [Reverse Shell](#reverse-shell-server-side) *- Server side. Includes **.exe***
  
- **[Cryptography](#cryptography)**
  - [Dencrypter](#dencrypter)
  
## Networking
### Network Scanner
This is a simple *airodump-ng* like **Network Scanner.** To use it you will have to install some libs like Scapy (the base of almost all networking Python scripts) and Pandas for formatted output.

#### **Use:** 

    sudo python3 network_scanner.py -i wlan0

You have to specify the NIC you are going to use and has to be in monitor mode.

### ARP Tool
These are some ARP utilities joined in a CLI tool. If you want to go for the full tool, check it's own repo here. In it's repo, all the code is explained and you can clone it for an easy installation.

Anyway, if you want to **use it as a Python script**, you can download the **[ARPTool](/ARPTool)** folder and run it like so.

**ARP Scan:** 

Use:

    sudo python3 arptool.py -s [target network/subnet]

Example:

    sudo python3 arptool.py -s 192.168.0.1/24

**ARP Spoof:** 

Use:

    sudo python3 arptool.py -t [victim's IP] -g [gateway IP]

Example:

    sudo pyhton3 arptool.py -t 192.168.0.20 -g 192.168.0.1

**ARP Spoof detection:**

Use: 

    sudo python3 arptool.py -d [NIC in monitor mode]
  
Example:

    sudo python3 arptool.py -d wlan0

I have uploaded the standalone scripts as well. Those are the ones in the **[/ARPTool/Scripts](/ARPTool/Scripts)** the folder:

 - [arpscan.py](/ARPTool/Scripts/arpscan.py)
 - [arpspoof.py](/ARPTool/Scripts/arpspoof.py)
 - [arpspoof_detect.py](/ARPTool/Scripts/arpspoof_detect.py)

And the use is similar to the **arptool.py** script. Just use the script you want to:

    sudo python3 [script.py] [--options]

### Simple Port Scanner
This is the script for a *goddamned-slow* port scanner. Why would you use this instead of **nmap**? Who knows, but the point for me was to learn how to code it!

#### Use:

    sudo python3 port_scanner.py [target IP] -p [ports range]

Example:

    sudo python3 port_scanner.py 192.168.0.1 -p 1,65535

### Packet Sniffer
This scripts is able to sniff HTTP packets and show interesting raw data if any. It only sniffs at port 80 as HTTPS packets (port 443) are encrypted so it's unuseful to sniff those.

#### Use:

    sudo python3 sniffer.py -i [NIC] -r

Example:

    sudo python3 sniffer.py -i wlan0 -r

This would be part of a future project I'm working on called **FartSuite.** You can imagine what kind tool I'm working on...

### DNS Spoofer

This script is able to perform a **DNS cache poisoning attack**. Well... kind of. It does perform the spoof attack **BUT** if the victim's browser has the website cached and it's a secure browser like **Chrome or Firefox**, the attack won't likely succeed.

I will work to improve that, I promise.

To use it, first you'll have to perform an ARP Spoofing attack with the [ARP Spoofing](#arp-tool) tool. This way you perform a **Man in the Middle** so now you can poison the DNS.

#### Use:

    sudo python3 dnsspoof.py -d [domain] -t [target IP]
    
> **Note:** In this script, the target IP is NOT the victim's IP but the IP where the victim will be redirected.

So, as an example of a common use would be: 
   1. Scan the network and choose your target
   2. Perform an ARP Spoofing attack 
   3. Run the DNS Spoofer script as explained above 
   4. And, to make sure it's working, you can start an Apache server locally and use that IP to redirect the traffic to.
   
Let your imagination fly...

