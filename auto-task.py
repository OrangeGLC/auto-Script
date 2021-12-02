#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from pymouse import PyMouse
import time
import os
import sys


#do action
def operate(act_type, *arg):    #x1=0, y1=0, x2=0, y2=0, loop="false", lpct=0, interval=0):
    #print("type = " + act_type + " arg = " + arg[0][0])
    if act_type == "click": 
        cmd = "adb shell input tap " + str(arg[0][0]) + " " + str(arg[0][1])
    elif act_type == "swipe": 
        cmd = "adb shell input swipe " + str(arg[0][0]) + " " + str(arg[0][1]) + " " + str(arg[0][2]) + " " +str(arg[0][3])
        os.system(cmd)
        time.sleep(2)
        return
    elif act_type == "back": 
        cmd = "adb shell input keyevent 4"
    elif act_type == "home": 
        cmd = "adb shell input keyevent 3"
    elif act_type == "sleep": 
        time.sleep(float(arg[0][0]))
        return
    elif act_type == "lauch": #Launch APP
        cmd = "adb shell am start -n " + arg[0][0]
    os.system(cmd)


def check_scrcpy_ststus():
    '''Plan B function, not use yet'''
    scp_status = os.popen("pgrep scrcpy").read()
    if len(scp_status) > 0:
        print("scrcpy's pid is " + scp_status)
        return True
    else:
        print("scrcpy is not running")
        return False


def exec_cmd_by_line(arg):
    '''exec one line cmd'''
    if len(arg) == 1:
        operate(arg[0])
    else:
        operate(arg[0], arg[1:])


def exec_all_cmd_line(line, start):
    if line[start].lstrip()[0:4] == "LOOP":
        if line[start][0:-1].split(': ')[1] == '*': #endless loop
            inloop = True
            lpct = 0
        else:   #limited loop
            inloop = False
            lpct = int(line[start][0:-1].split(': ')[1][0:])
    else: #only exec once
        lpct = 1
        start -= 1 #avoid skipping first line cmd

    
    while lpct != 0 or inloop:
        i = start + 1 #loop start location
        while True:
            if i >= len(line):  #exec finish
                exit()
            if line[i].lstrip()[0] == '#':
                print(line[i].rstrip())
            elif line[i].lstrip()[0:4] == "LOOP":
                i = exec_all_cmd_line(line, i) #Save exec site in variable i, then next round will exec from here
            elif line[i].lstrip()[0:3] == "END":
                break
            else:
                arg = line[i].lstrip().rstrip().split(", ")
                exec_cmd_by_line(arg)
                time.sleep(1)
            i += 1
        if lpct != 0:
            lpct -= 1
    return i
    
def main():
    '''read action from file'''
    filename = sys.argv[1]
    with open(filename) as file:
        line = file.readlines()

    '''exec each line'''
    exec_all_cmd_line(line, 0)


if __name__ == '__main__':
    main()
