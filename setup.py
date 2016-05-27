"""This will install necessary dependencies on the local machine"""
import os
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
os.system("sudo easy_install pip")
os.system("sudo pip install pyperclip")
print bcolors.OKGREEN + "Ready to run C M D R!" + bcolors.ENDC
