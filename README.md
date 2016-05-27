#[C M D R] | Quick Command Copy

description     : Server-side Command/Text Repository and Copy

version         : V - 0.5 - Alpha

author          : Josh Bray

site            : cryptodoom.com

date            : 06.27.16

usage           : python cmdr.py

GitHub          : github.com/cryptodoom/cmdr

python_version  : 2.7.6


#Install/Run

1) On local machine run setup.py

'python setup.py'


2) Add your text to the cmdr.py script.

'nano cmdr.py'


3) Move cmdr.py to necessary location where you will need to access the script.

'mv cmdr.py /path/to/location/'


4) Run 'python cmdr.py'


#Needs Fixing:

1) When in a category, can select another category.  This needs to be disabled so once on a category they have to chose a command or back/q.

2) When command is selected and after copied to keyboard, program should quit and print 'command copied'.  As of now it returns to main screen.

3) Need to figure out how to store/retreive awk/bash lines of commands without formatting/errors thrown.

#Needs Improving:

1) The way the commands are stored.  May look at using a dictionary or mySQL for storage/retevial.

