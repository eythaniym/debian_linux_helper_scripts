#! /usr/bin/python3

__license__ = "MIT"

import os

# Welcome
print("\n\n")
print(" _______  __   __  _______  _______       _______  _______  _______     _______  _______  ______    ___  _______  _______ ")
print("|   _   ||  | |  ||       ||       |     |   _   ||       ||       |   |       ||       ||    _ |  |   ||       ||       |")
print("|  |_|  ||  | |  ||_     _||   _   |     |  |_|  ||    _  ||_     _|   |  _____||       ||   | ||  |   ||    _  ||_     _|")
print("|       ||  |_|  |  |   |  |  | |  |     |       ||   |_| |  |   |     | |_____ |       ||   |_||_ |   ||   |_| |  |   |  ")
print("|       ||       |  |   |  |  |_|  | ___ |       ||    ___|  |   | ___ |_____  ||      _||    __  ||   ||    ___|  |   |  ")
print("|   _   ||       |  |   |  |       ||   ||   _   ||   |      |   ||   | _____| ||     |_ |   |  | ||   ||   |      |   |  ")
print("|__| |__||_______|  |___|  |_______||___||__| |__||___|      |___||___||_______||_______||___|  |_||___||___|      |___|")
print("\n\t\t\t\tNOTE: Run script as sudo")
print("\n\n")

# Script
print("\tAPT UPDATE")
os.system("apt update -y")
print("\n\tAPT UPGRADE")
os.system("apt upgrade -y")
print("\n\tAPT FULL-UPGRADE (DIST-UPGRADE)")
os.system("apt full-upgrade -y")
print("\n\tAPT AUTOREMOVE")
os.system("apt autoremove -y")
print("\n\tDone!")
