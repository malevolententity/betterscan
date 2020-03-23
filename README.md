# betterscan
A simple script I use alot when playing HackTheBox where nmap is too slow to do a full port scan in most cases

The script will create a "masscan.txt" file containing output of masscan and parses the file for the open ports. It then feeds those ports to nmap with the following options:

``` 
nmap -A -T4 
``` 

### Usage:

```
sudo python betterscan.py <IP_Address

e.g.

sudo python betterscan.py 10.10.10.151
```

### Prerequisites

1. masscan 
2. nmap
3. python2.7
