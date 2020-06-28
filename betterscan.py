#!/usr/bin/env python 
import os, sys, threading
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port-file", help="file containing ports scanned by massmap. If specified, skips massscan and goes directly to nmap")
parser.add_argument("-o", "--options", help="specifies options that nmap should run. e.g. -A -T4. DO NOT SPECIFY PORTS")



parser.add_argument("-e", "--interface", help="interface to perform the scan on e.g. wlan0", required=True)
parser.add_argument("ip", help="IP address to perform nmap on.")
args = parser.parse_args()



print "Checking if " + args.ip + " is up...."
#To check if host is up else exit
HOST_UP  = True if os.system("ping -c 2 " + args.ip.strip(";") + ">/dev/null 2>&1") is 0 else False

if HOST_UP:
	print args.ip + " is reachable. Starting betterscan"
else:
	print "ERROR: IP unreachable. Exiting"
	exit()



if args.port_file is None:
# ################
# # MASSCAN PART #
# ################
	with open("masscan.txt", "w+") as f:
		cmd = "sudo masscan -p1-65535,U:1-65535 --rate=1000 --wait 0 -e" + args.interface + " " + args.ip
		subprocess.call(cmd, stdout=f, shell=True)


print "[+] Directory: " + os.getcwd() + "/masscan.txt"

#############
# NMAP PART #
#############
ports = []
for line in open (os.getcwd() + "/masscan.txt"):

	#get the port/tcp string
	port = line.split(" ")[3]
	#remove /tcp and /udp from the string
	port = port.split("/")[0]
	ports.append(int(port))

ports.sort()


if len(ports) <= 0:
	print "ERROR: Empty port list. Exiting."
	exit()

if args.options is None:
	options = ""
else:
	options = args.options

cmd = "nmap " + options + " -p" + ",".join(map(str,ports)) + " " + args.ip
subprocess.call(cmd, shell=True)




