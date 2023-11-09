#!/bin/bash
MAC=$1
# List network interface names
iface_names=($(ip link show | grep '^[0-9][0-9]*:' | awk -F':' '{print $2}'|awk '{$1=$1};1'))

#interface_names=($(ip link show | awk -F: '$0 !~ "lo|vir|docker|en" {print $2}'))

# Iterate through interface names and ping them
for iface in "${iface_names[@]}"; do
    echo "Pinging -$MAC-$1 via $iface ..."
    sudo arping -c 2 -I $iface $MAC  # Change the target IP address if needed
    echo "----------------------------------------"
done
