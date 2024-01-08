![Python Hacking Tools](/img/banner.png)

<div align="center">

![python](https://img.shields.io/badge/Python-3.11-FFDA4A.svg?style=flat&logo=python&logoColor=white&labelColor=blue)
![tested](https://img.shields.io/badge/tested-locally-green) 
![OS](https://img.shields.io/badge/OS-Kali_Linux-blue)
![OS](https://img.shields.io/badge/OS-Ubuntu-orange)

</div>

These are some of the python tools and scripts I have crafted so far. I will be updating the repo as I code more or if any update needs to be made.

Some of them may have their own repo for further explanation/ease of installation (as in the case of the CLI tools).

> [!NOTE]
> I know many of the scripts are not precisely clean neither efficient. This is because they were coded in a rush during some jobs and fastly and poorly cleaned afterwards. My apologies.

If you are promped with any error when running any script, check the error, it might be due to any library missing. As in the case of the keylogger as you must install the keyboard package for python.

## Index 
Groups and categories might not be the most correct ones. Any correction/suggestion is welcome!

- **[Networking](#networking)** 
  - [Network Scanner](#network-scanner)
  - [ARPTool](#arp-tool) - *CLI tool + individual scripts* 
    - *ARP Scanner*
    - *ARP Spoofer*
    - *ARP Spoofing detection*
  - [Simple Port Scanner](#simple-port-scanner)
  - [Packet Sniffer](#packet-sniffer)
  - [DNS Spoofer](#dns-spoofer)
  - [FakeAP](#fakeap) *- Further features under development*
  - [Deauther](#deauther) *- Check [here](https://github.com/amtzespinosa/esp8266-wifi-deauther) the hardware version with an **ESP-8266*** 
  - [MAC Changer](#mac-changer)

- **[Web Pentesting](#web-pentesting)**
  - [DNS Tool](#dns-tool) - *CLI tool + individual scripts* 
  - [Subdomain Finder](#subdomain-finder)
  - [Link Extractor](#link-extractor)
  - [XSS Scanner](#xss-scanner)
  - [SQL Injector](#sql-injector)

- **[Brute Force](#brute-force)**
  - [SSH Brute Force](#ssh-brute-force)

- **[Remote Access](#remote-access)**
  - [Reverse Shell](#reverse-shell-client-side) *- Attacker's side*
  
- **[Payloads](#payloads)**
  - [Keylogger](#keylogger)
  - [Reverse Shell](#reverse-shell-server-side) *- Victim's side*

> Coming soon: Stealthy **.exe** for both scripts so they can be run in the background
  
- **[Hiding Data](#hiding-data)**
  - [Dencrypter](#dencrypter)

- **[Communications](#communications)**
  - [Encrypted Chat](#encrypted-chat)  - *PoC*
  
## Networking
### Network Scanner
This is a simple *airodump-ng* like **Network Scanner.** To use it you will have to install some libs like Scapy (the base of almost all networking Python scripts) and Pandas for formatted output.

#### **Use:** 

    sudo python3 network_scanner.py -i wlan0

You have to specify the NIC you are going to use and has to be in **monitor mode.**

### ARP Tool

**Installation**

Download the `arptool.zip` inside **[ARPTool](/Networking/ARPTool/CLI/)** folder. Once decompressed, run `sudo bash install.sh`. This script will make it easier to execute the tool through the terminal but you can still execute the tool as a Python script. If you want to uninstall **arptool** just run the command `arptool-uninstall`. 

**ARP Scan:** 

Use:

    sudo arptool -s [target network/subnet]

Example:

    sudo arptool -s 192.168.0.1/24
    
![ARP Scan output](/outputs/arpscan.png)

**ARP Spoof:** 

Use:

    sudo arptool -t [victim's IP] -g [gateway IP]

Example:

    sudo arptool -t 192.168.0.20 -g 192.168.0.1

![ARP Spoof output](/outputs/arpspoof.png)

**ARP Spoof detection:**

Use: 

    sudo arptool -d [NIC]
  
Example:

    sudo arptool -d wlan0

![ARP Spoof Detection output](/outputs/arpdetect.png)

I have uploaded the standalone scripts as well. Those are the ones in the **[/ARPTool](/ARPTool)** folder:

 - [arpscan.py](/ARPTool/arpscan.py)
 - [arpspoof.py](/ARPTool/arpspoof.py)
 - [arpspoof_detect.py](/ARPTool/arpspoof_detect.py)

And the use is similar to the **arptool.py** script. Just use the script you want to:

    sudo python3 [script.py] [--options]

### Simple Port Scanner
This is the script for a *goddamned-slow* port scanner. Why would you use this instead of **nmap**? Who knows, but the point for me was to learn how to code it!

#### Use:

    sudo python3 port_scanner.py [target IP] -p [ports range]

#### Example:

    sudo python3 port_scanner.py 192.168.0.1 -p 1,65535

![Port Scanner output](/outputs/portscanner.png)

### Packet Sniffer
This scripts is able to sniff HTTP packets and show interesting raw data if any. It only sniffs at port 80 as HTTPS packets (port 443) are encrypted so it's unuseful to sniff those. To sniff packets from a specific host you need to be a **Man in the Middle.** You can achieve so with an ARP Spoofing attack.

#### Use:

    sudo python3 sniffer.py -i [NIC] -r

#### Example:

    sudo python3 sniffer.py -i wlan0 -r

![Sniffer output](/outputs/sniff.png)

This would be part of a future project I'm working on called **FartSuite.** You can imagine what kind tool I'm working on...

### DNS Spoofer

This script is able to perform a **DNS cache poisoning attack**. Well... kind of. It does perform the spoof attack **BUT** if the victim's browser has the website cached and it's a secure browser like **Chrome or Firefox**, the attack won't likely succeed.

I will work to improve that, I promise.

To use it, first you'll have to perform an ARP Spoofing attack with the [ARP Spoofing](#arp-tool) tool. This way you perform a **Man in the Middle** so now you can poison the DNS.

#### Use:

    sudo python3 dnsspoof.py -d [domain] -t [target IP]
    
> **Note:** In this script, the target IP is NOT the victim's IP but the IP where the victim will be redirected.

So, as an example of a common use would be: 
   1. Scan the network with ARP Scanner and choose your target
   2. Perform an ARP Spoofing attack 
   3. Run the DNS Spoofer script as explained above 
   4. And, to make sure it's working, you can start an Apache server locally and use that IP to redirect the traffic to.
   
Let your imagination fly...

### FakeAP

> **Note:** FakeAP is currently under further development.

By now, the script is only able to set fake APs with no internet connection neither password. 

I am trying to make it perform better so it would be able to set a rogue AP with internet conection and password in order to perform **Evil Twin** attacks.

In the meanwhile...

#### Use:

    sudo python3 fap.py -s [SSID] -i [NIC in monitor mode]

#### Example:

    sudo python3 fap.py -s FakeAP -i wlan0

### Deauther

This is a simple yet effective deauther able to perform a complete DoS on a network without being logged into the network.

#### Use: 

    sudo python3 deauther.py -t [target gateway MAC] -i [NIC in monitor mode] -c [amount of packets to send]

The time of the DoS will depend on how many packets you send. 100 packets is a 10 seconds DoS. 

#### Example:

    sudo python3 deauther.py -t FA:KE:MA:CA:DD:RS -i wlan0 -c 10000

### MAC Changer

Simple MAC changing script. You can change your MAC to a random one or to a specific one.

#### Use: 

    sudo python3 machanger.py -i [NIC] -r [for random MAC]/-m [MAC to change to]

#### Example:

Random MAC:

    sudo python3 machanger.py -i wlan0 -r

Specific MAC:

    sudo python3 machanger.py -i wlan0 -m FA:KE:MA:CA:DD:RS

## Web Pentesting

### DNS Tool

**Installation**

Download the `dnsrecon.zip` inside **[DNS Tool](</Web Pentesting/DNS Tool/CLI/>)** folder. Once decompressed, run `sudo bash install.sh`. This script will make it easier to execute the tool through the terminal but you can still execute the tool as a Python script. If you want to uninstall **dsnrecon** just run the command `dsnrecon-uninstall`. 

You can use the individual Python scripts as well.

**Info:** 

Use:

    sudo dsnrecon info -d [domain]

Example:

    sudo dsnrecon info -d github.com
    
![DNS enum output](/outputs/dnsenum.png)

**Enum:** 

Use:

    sudo dsnrecon enum -d [domain]

Example:

    sudo dsnrecon enum -d github.com

### Subdomain Finder

This tool is a simple subdomain finder via dictionary (brute force). It is quite fast and efficient. I have provided you with a little 10k subdomains dictionary for you to try it.

#### Use:

    sudo python3 subfinder.py -d [domain] -w [dictionary file]

#### Example:

    sudo python3 subfinder.py -d github.com -w sub10k.txt

![Subfinder output](/outputs/subfinder.png)

It is a multi-thread script and you can set the number of threads with the optional argument **-t** - default is 10. You can as well save the output in a file with the optional argument **-o**.

#### Example:

    sudo python3 subfinder.py -d github.com -w sub10k.txt -t 100 -o sub_found.txt

### Link Extractor

It might look more like an SEO utility but this script is quite useful for listing directories from a website. You must be careful on big websites, although you can pass a depth parameter to the script, if the website has a lot of links it will recursively check them all. You can as well send the output to a file with the optional **-o** parameter.

> **NOTE:**
>
> To use this script you'll have to install beautifulsoup4: **sudo pip3 install beautifulsoup4**.

#### Use:

    sudo python3 linkextractor.py -u [URL] -d [depth] -o [filename]

#### Example:

    sudo python3 linkextractor.py -u https://github.com -d 1 -o directories.txt

![Link extractor output](/outputs/linkextractor.png)

### XSS Scanner

A simple **XSS Vulnerabilities** scanner. This scanner as well as the **SQLi** scanner are mainly Proof of Concepts as they work but they're not reliable at all. I may improve them in a future.

#### Use:

    sudo python3 xsscan.py -u [URL] 

#### Example:

    sudo python3 xsscan.py -u http://testphp.vulnweb.com/

![XSS scan output](/outputs/xss.png)

### SQL Injector

Named after a **Thrash Metal** band from Cartagena, Spain, here's my simple **SQLi** scanner. Like said before, it's not reliable by any means but serves as a PoC.

#### Use:

    sudo python3 injector.py -u [URL] 

#### Example:

    sudo python3 injector.py -u http://testphp.vulnweb.com/artists.php?artist=1

![SQLi output](/outputs/sqli.png)

## Brute Force
### SSH Brute Force

Simple SSH login brute force script. Nothing new under the sun!

#### Use: 

    sudo python3 sshbruteforce.py -u/U [single user/user list] -P [password list]

## Remote Access
### Reverse Shell (Client Side)

This is the code for a shell able to execute commands in the victim's machine. Use is pretty simple as you just need to run  the script. By default it will listen to incoming connections from all NIC IPs and at port 5003.

#### Use:

    sudo python3 reverse_shell_client.py

And that's it. This way, as soon as the victim starts the other half of the script, you will have access to all it's OS avoiding Firewalls protection.

Soon I will implement the possibility of changing IP and port via CLI commands.

![Reverse Shell output](/outputs/revclient.png)

## Payloads
### Keylogger

A simple keylogger that registers keystrokes and sends them to an email address once every 60 seconds. You may want to change this parameter indicated in the code.

#### Use: 

    sudo python3 keylogger.py

If you pack it into an **exe** before I do and want to contribute, it will be welcomed!

### Reverse Shell (Server Side)
The other part of the reverse shell. Same usage as the one mentioned above. Also if you pack it into a **dll** or **exe** in order to make an effective payload and want to contribute, just let me know.

![Reverse Shell output](/outputs/revserver.png)

## Hiding Data
### Dencrypter

This tool helps you generate keys to encrypt and decrypt files.

**Generating a key**

Use:

    sudo python3 dencrypter.py -g [key filename]

Example

    sudo python3 dencrypter.py -g key1.key

**Encrypting a file**

Use:

    sudo python3 dencrypter.py -e [file to encrypt] -k [key file to use for encryption]

Example:

    sudo python3 dencrypter.py -e secretfile.txt -k key1.key

**Decrypting a file**

Use:

    sudo python3 dencrypter.py -d [file to decrypt] -k [key file to use for decryption]

Example:

    sudo python3 dencrypter.py -d secretfile.txt -k key1.key

## Communications
### Encrypted Chat

Two scripts: one for the server and another one for the clients. The messages are encrypted and decrypted within the client script so they can only be read by the ones who have acces to the key.

The key is hardcoded in the script. Not safe at all but it's a good PoC of how to make secure comms.

> **Note:** To use it from outside your LAN you'll have to make some modifications. These scripts have been tested within the same virtual machine!

#### Use:

To use them, just run the scripts. They will be further improved to be able to choose the IP of the server room to connect to when running the script. 
