#!/bin/bash
#fileName: ipRouter.sh
#author: Hezha
#dateAndTime: 1/25/24-15:48
#description: This program take destination ip address and your router and write it to the route table.

#check if the program has root privilage
if [["$EUID" -ne 0]]; then
    echo "Please run the script with root privilages."
    exit 1
fi

#error handler
if [["$#" -ne 2]]; then
    echo "Usage: $0 [ip1] [ip2]"
    exit 1
fi

ip1="$1"
ip2="$2"

ip route add "$ip1" via "$ip2"
echo "Route added: $ip1 via $ip2"
