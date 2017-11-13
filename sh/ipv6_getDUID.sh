#!/bin/bash
if [ -x "$(which hexdump)" ]; then
               if [ -f "/var/lib/dhcpv6/dhcp6c_duid" ]; then
                              string=$(hexdump /var/lib/dhcpv6/dhcp6c_duid | head -n1 | cut -d' ' -f3-)
               else
                              echo "Missing /var/lib/dhcpv6/dhcp6c_duid"
                              exit 1
               fi
               DUID=""
               for item in $string; do
                              part1=$(echo -n "$item" | cut -b3,4)
                              part2=$(echo -n "$item" | cut -b1,2)
                              DUID="$DUID:$part1:$part2"
                              part1=""
                              part2=""
               done
               DUIDfinal=$(echo $DUID | cut -b2-)
               echo $DUIDfinal
else
               echo "apt-get install hexdump .. and try again"
               exit 1
fi

