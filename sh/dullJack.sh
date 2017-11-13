#!/bin/bash

tput civis; clear;
orig='all work and no play makes Jack a dull boy. All Work and no play MAKES jaCK a dull boy. All WORK and NO PLAY makes JACk a DUll BOY! All work and no PLAY makes Jakc a dull Boy. All Work and Npo Play makes Jack a dull boy. ALL WORK and no PLAY makes jacK a dull boY! .. All work and no play makes Jak a dull Boy.   '
msg=$(echo $orig | sed -e 's/\ /_/g')
length=${#msg}

for i in `seq 0 $length`; do
        sleep 0.1
        letter=${msg:$i:1}

        if [ letter = "_" ]; then
                letter=" ";
        fi
        echo -n $letter | sed -e 's/_/\ /g'

done

