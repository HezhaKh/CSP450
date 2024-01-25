#!/usr/bin/env python3
"""
fileName: sshdConf.py
author: Hezha
dateAndTime: 1/25/24-10:45
description: This program disables the rootSSH and PasswdSSH
"""
from os import geteuid as euid
def createConfigFile():
    filePath="/etc/ssh/sshd_config.d/10-noRootLogin"
    config="Port 22\n# Auth\nPermitRootLogin no\n# Disble Password\nPasswordAuthentication no\n# challenge-response passsword (could over-ride )\nKbdInteractiveAuthentication no\n"

def main():
    try:
        if euid == 0:
            createConfigFile()
            print(f"The {createConfigFile.filePath()} was created.")
        else:
            print("please run the program with the root privilages.")
    except:
        print("please run the program with the root privilages.")

if __name__=="__main__":
    main()