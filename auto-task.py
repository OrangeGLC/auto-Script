#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymouse import PyMouse
import time
import os
import sys

#unlock


#launch app

#do action
def operate(act_type, x1=0, y1=0, x2=0, y2=0, loop="false", lpct=0, interval=0):
    if act_type == 1: #click
        cmd = "adb shell input tap " + str(x1) + " " + str(y1)
    elif act_type == 2: #swipe
        cmd = "adb shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " +str(y2)
        os.system(cmd)
        time.sleep(2)
        return
    elif act_type == 3: #back
        cmd = "adb shell input keyevent 4"
    elif act_type == 4: #home
        cmd = "adb shell input keyevent 3"
    elif act_type == 5: #sleep
        time.sleep(x1)
        return
    if lpct > 0 and loop == "True":
        while lpct > 0:
            os.system(cmd)
            time.sleep(interval)
            lpct -= 1
    else:
        os.system(cmd)

def check_scrcpy_ststus():
    """Check scrcpy launch status"""
    scp_status = os.popen("pgrep scrcpy").read()
    if len(scp_status) > 0:
        print("scrcpy's pid is " + scp_status)
        return True
    else:
        print("scrcpy is not running")
        return False

def main():
    #operate(1, 540, 1910, 0, 0, True, 30, 1)
    '''read action from file'''
    filename = sys.argv[1]
    with open(filename) as file:
        for line in file:
            if line[0] == '#':
                print(line)
                continue
            arg = line[0:-1].split(', ')
            print(arg)
            if len(arg) == 1:
                operate(int(arg[0]))
            elif len(arg) == 2:
                operate(int(arg[0]), int(arg[1]))
            elif len(arg) == 3:
                operate(int(arg[0]), int(arg[1]), int(arg[2]))
            elif len(arg) == 5:
                operate(int(arg[0]), int(arg[1]), int(arg[2]), int(arg[3]), int(arg[4]))
            else:
                operate(int(arg[0]), int(arg[1]), int(arg[2]), int(arg[3]), int(arg[4]), arg[5], int(arg[6]), float(arg[7]))
            time.sleep(0.8)

if __name__ == '__main__':
    main()
