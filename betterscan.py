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
with open("massscan.txt", "w+") as f:
	cmd = "sudo masscan -p1-65535,U:1-65535 " + args.ip + " --rate=1000 -e tun0"
	subprocess.call([cmd], stdout=f, shell=True)

#############
# NMAP PART #
#############

ports = []
for line in open ("massscan.txt"):

	#get the port/tcp string
	port = line.split(" ")[3]
	#remove /tcp and /udp from the string
	port = port.split("/")[0]
	ports.append(int(port))
ports.sort()
nmap_cmd = "nmap -A -T4 -p" + ",".join(map(str,ports)) + " " + args.ip

p = subprocess.Popen(nmap_cmd, shell=True)
p.wait()




