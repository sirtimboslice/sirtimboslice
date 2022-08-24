#!/bin/bash


if [ "$1" == "" ]; then
echo "You did not enter an IP address"
echo "Syntax: ./ping_sweep.sh 192.168.1 ip_list.txt"
echo "Only enter the first 3 octets of the IPv4 address"


elif [ "$2" == "" ] ; then
echo "You did not enter the output file name"
echo "Syntax: ./ping_sweep.sh 192.168.1 ip_list.txt"

else
echo "Script working. Please wait..."
for i in `seq 1 254`; do
ping -c 1 $1.$i | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"  >> $2 &
done

for ip in $(cat $2); do nmap $ip >> scan_out.txt; done
fi

