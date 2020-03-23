#!/usr/bin/env python 
import sys
import argparse
import subprocess


parser = argparse.ArgumentParser()
#parser.add_argument("port_list", help="file containing ports scanned by massmap")
parser.add_argument("ip", help="IP address to perform nmap on.")
args = parser.parse_args()

################
# MASSCAN PART #
################
with open("masscan.txt", "w+") as f:
	cmd = "sudo masscan -p1-65535,U:1-65535 --rate=1000 --wait 0 -e tun0 " + args.ip
	subprocess.call(cmd, stdout=f, shell=True)

#############
# NMAP PART #
#############

ports = []
for line in open ("masscan.txt"):

	#get the port/tcp string
	port = line.split(" ")[3]
	#remove /tcp and /udp from the string
	port = port.split("/")[0]
	ports.append(int(port))

ports.sort()

cmd = "nmap -A -T4 -v -p" + ",".join(map(str,ports)) + " " + args.ip
subprocess.call(cmd, shell=True)




