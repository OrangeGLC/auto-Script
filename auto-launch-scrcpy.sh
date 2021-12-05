#!/bin/bash
logfile=/tmp/autoscrcpy.log
logline=0
while true
do
    devNum=$[ $(adb devices |wc -l)-2]
    if [ $devNum -ge 1 ]
    then
        echo "$(date) Find ${devNum} device" >> $logfile
        echo "$(date) Launch scrcpy ..." >> $logfile
        scrcpy -b 2M -m 1024 --max-fps 60 --window-x 0 --window-y 0 --always-on-top -w >> $logfile
#    else
#        echo "Can not find any devices!"
    fi
    if [ -e $logfile ]
    then
        logline=$[ $(cat $logfile|wc -l)]
    fi
    if [ $logline -gt 50000 ]
    then
        rm -rf $logfile
        echo "$(date) too large log should be delete!"
    fi
    sleep 5
done

