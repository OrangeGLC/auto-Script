#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymouse import PyMouse
import time
import os

#unlock


#launch app


#do action



def check_scrcpy_ststus():
    """Check scrcpy launch status"""
    scp_status = os.popen("pgrep scrcpy").read()
    if(len(scp_status) > 0):
        print("scrcpy's pid is " + scp_status)
        return True
    else:
        print("scrcpy is not running")
        return False

def main():
    while (check_scrcpy_ststus()):
        print("scrcpy is running")
        time.sleep(3)
        

if __name__ == '__main__':
    main()