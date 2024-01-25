#!/usr/bin/env python3
"""
fileName: sudoNoPass.py
author: Hezha
dateAndTime: 1/25/24-00:40
description: This program asks for a username to give it sudo with no password privilage.
"""
from os import geteuid as euid

def addUserToSudoers(username):                                     #create the file and the content
    filepath=f"/etc/sudoers.d/10-csp-{username}"
    with open(filepath, "w") as f:
        f.write(f"{username} ALL=(ALL) NOPASSWD:ALL\n")

def main():
    try:                                                            #error handler 
        euid()==0                                                   #check if the program is running with root privilages
        username=input("Please enter your target username: ")
        if username:                                                #ask for user input and print the resualts
            addUserToSudoers(username)
            print(f"The user [{username}] has been added to the sudoers with no password.")
        else:
            print("No username entered. Exiting.")
    except:
        print("Please run this program with root privilages!")