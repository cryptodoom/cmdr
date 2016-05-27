#github.com/cryptodoom/cmdr/
"""This will install necessary dependencies on the local machine"""
import os

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

#Linux pip install
os.system("sudo apt-get install python-pip -y")
#OSX pip install
os.system("sudo easy_install pip")
#Pyperclip install
os.system("sudo pip install pyperclip")
#Success Message
print bcolors.OKGREEN + "Ready to run C M D R!" + bcolors.ENDC
