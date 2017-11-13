#!/bin/bash
bccmd=`which bc`

if [ -x "$bccmd" ]; then

        DNSSERVER="8.8.8.8"
        echo "Using DNS server $DNSSERVER for requests"
        echo "----------------------------------------"
        fail=0

        for i in `seq 1 100`; do
            START=$(date +%s.%N) && dns=$(dig @$DNSSERVER vg.no | grep "Query time:" ) && END=$(date +%s.%N)
                # echo $START echo $END
                DIFF=$(echo "$END - $START" | bc)
                    if [ "$dns" != "" ]; then
                                echo "$i : cmd time (sec) $DIFF dig: $dns" | sed -e 's/;//g'
                        else
                                echo "$i : cmd FAILED dig: TIMEOUT"
                                let fail=$fail+1
                        fi
                        dns="";
        done

        echo "$fail/$i UDP/53 pakker tapt"
else
        echo "Kommandoen bc er ikke installert, installer med: apt-get install."
        echo "Konfigurert DNS server å teste mot er $DNSSERVER"
fi

