#!/usr/bin/env python 
import os, sys, threading
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--port-file", help="file containing ports scanned by massmap. If specified, skips massscan and goes directly to nmap")
parser.add_argument("options", help="specifies options that nmap should run. e.g. -A -T4. DO NOT SPECIFY PORTS")
parser.add_argument("ip", help="IP address to perform nmap on.")
args = parser.parse_args()

print args.options 

print "Checking if " + args.ip + " is up...."



ports = []
# for line in open (os.getcwd() + "/masscan.txt"):

# 	#get the port/tcp string
# 	port = line.split(" ")[3]
# 	#remove /tcp and /udp from the string
# 	port = port.split("/")[0]
# 	ports.append(int(port))

# ports.sort()

cmd = "nmap " + args.options + " " + args.ip
print cmd
#subprocess.call(cmd, shell=True)
