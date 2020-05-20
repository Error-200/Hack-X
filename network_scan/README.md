# NETWORK SCANNER


A network scanner is one major tool for analyzing the hosts that are available on the same network. A network scanner is an IP scanner that is used for scanning the networks that are connected to several computers, with th help of ARP protocol this tool also fetch MAC address of the device. 



## RUN 


1. Clone the repo 

```bash
root@kali:~# git clone https://github.com/Error-200/Hack-X.git

```
2. Change the dir 

```bash
root@kali:~#  cd Hack-X
root@kali:~/Hack-X#  cd network_scan

```
3. Run the command to scan the devices

```bash
root@kali:~/Hack-X/network_scan#  python network_scanner.py  --target (your IP range)

```
example: 

```bash

root@kali:~/Hack-X/network_scan#  python network_scanner.py  --target 10.0.2.1/24

```

### BUILD WITH 

- Python
- Python modules used 

  - [scapy](https://scapy.readthedocs.io/en/latest/)
  - [argparse](https://docs.python.org/3/library/argparse.html)
