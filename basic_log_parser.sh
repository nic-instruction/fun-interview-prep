#!/bin/bash

#cuz this looks kinda fun :)
# Jan 10 20:22:13 imago rtkit-daemon[1094]: Supervising 4 threads of 3 processes of 1 users.

while read -r month dayOfMonth time machine process entry
do
        #echo "there's some stuff in here.... um..."
        #echo "entry lools like $entry"
        #echo "$month"
        if [ "$entry" == "Started Tracker metadata extractor." ];
        then
                echo "$machine, $time, $dayOfMonth"
        fi
done < <(cat /var/log/syslog)

# Super simple and effective.  That was incredibly easy and fun... going to try that in python as well...
