#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           : [C M D R] | Quick Command Copy
#description     : Server-side Command Repository and Copy
#author          : Josh Bray
#site            : cryptodoom.com
#date            : 06.27.16
#usage           : python cmdr.py
#GitHub          : github.com/cryptodoom/cmdr
#python_version  : 2.7.6
### Imports
# Data Structure
import sys, os
# Copy to Clipboard
import pyperclip
# Help -h
import argparse
### Define taglines
info = "Version Info, Changelog, and more information available at: github.com/cryptodoom/cmdr"
title = "C M D R | Quick Command Copy"
bar = (30 * '-')
### Help
parser=argparse.ArgumentParser(
    description='''C M D R (Commander) Help''',
    epilog=info)
args=parser.parse_args()
### Main definitions - constants
menu_actions  = {}
# Back to main menu
def back():
    menu_actions['main_menu']()
# Exit program
def exit():
    sys.exit()
###Style
class color:
   DARKCYAN = '\033[36m'
   END = '\033[0m'
# =======================
#     Category FUNCTIONS
# =======================
### Title - Main Category Select
def main_menu():
    os.system('clear')
    print
    print color.DARKCYAN + title + color.END
    print bar
### List Categories
    print "[a] Category Alpha"
    print "[b] Category Bravo"
    print "[c] Category Charlie"
    print bar
    print "[q]uit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
### Choose a Category
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return
# =======================
#       Categories
# =======================
# Category One
def category_alpha():
    print "Category Alpha - Title"
    print bar
    print "1. First Command - Category Alpha"
    print "2. Second Command - Category Alpha"
    print "[<] back"
    print "[q]uit"
    choice = raw_input(">> ")
    if choice == "1":
        pyperclip.copy("First Command - Category Alpha - Command Copied!")
        spam = pyperclip.paste()
    elif choice == "2":
        pyperclip.copy("Second Command - Category Alpha - Command Copied!")
        spam = pyperclip.paste()
    else:
        print "You didn't pick left or right! Try again."
    exec_menu(choice)
    return
# Category Two
def category_bravo():
    print "Category_Bravo - Title"
    print bar
    print "1. First Command - Category Bravo"
    print "2. Second Command - Category Bravo"
    print "3. Third Command - Category Bravo"
    print "[<] back"
    print "[q]uit"
    choice = raw_input(">> ")
    if choice == "1":
        pyperclip.copy("Second Command - Category Bravo - Command Copied!")
        spam = pyperclip.paste()
    elif choice == "2":
        pyperclip.copy("Second Command - Category Bravo - Command Copied!")
        spam = pyperclip.paste()
    elif choice == "3":
        pyperclip.copy("Third Command - Category Bravo - Command Copied!")
        spam = pyperclip.paste()
    else:
        print "Invalid selection, please try again.\n"
    exec_menu(choice)
    return
# Category Three
def category_charlie():
    print "Category Charlie - Title"
    print bar
    print "1. First Command - Category Charlie"
    print "2. Second Command - Category Charlie"
    print "3. Third Command - Category Charlie"
    print "4. Fourth Command - Category Charlie"
    print "[<] back"
    print "[q]uit"
    choice = raw_input(">> ")
    if choice == "1":
        pyperclip.copy("Second Command - Category Charlie - Command Copied!")
        spam = pyperclip.paste()
    elif choice == "2":
        pyperclip.copy("Second Command - Category Charlie - Command Copied!")
        spam = pyperclip.paste()
    elif choice == "3":
        pyperclip.copy("Third Command - Category Charlie - Command Copied!")
        spam = pyperclip.paste()
    elif choice == "4":
        pyperclip.copy("Fourth Command - Category Charlie - Command Copied!")
        spam = pyperclip.paste()
    else:
        print "Invalid selection, please try again.\n"
    exec_menu(choice)
    return
# =======================
#    Category/Direction
# =======================
# Choose Category Dictionary
menu_actions = {
    'main_menu': main_menu,
    '<': back,
    'q': exit,
    'a': category_alpha,
    'b': category_bravo,
    'c': category_charlie,
}
# =======================
#      MAIN PROGRAM
# =======================
# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
