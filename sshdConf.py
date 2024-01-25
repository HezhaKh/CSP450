#!/usr/bin/env python3
"""
fileName: sshdConf.py
author: Hezha
dateAndTime: 1/25/24-10:45
description: This program disables the rootSSH and PasswdSSH
"""
from os import geteuid as euid

def createConfigFile():                                         #create the file and return the file path
    filePath="/etc/ssh/sshd_config.d/10-noRootLogin"
    config="Port 22\n# Auth\nPermitRootLogin no\n# Disble Password\nPasswordAuthentication no\n# challenge-response passsword (could over-ride )\nKbdInteractiveAuthentication no\n"
    with open(filePath, "w") as file:
        file.write(config)
    return filePath

def main():                                                     #check for the privilages and error handling
    if euid()==0:
            thePath=createConfigFile()
            print(f"The [{thePath}] was created.")
    else:
            print("please run the program with the root privilages.")

if __name__=="__main__":
    main()