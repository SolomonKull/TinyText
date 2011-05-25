#!/usr/bin/env python

#########################################
### TinyText 1.0 ########################
### Copyright (C) 2011 ##################
### SolomonKull <solomonkull@gmail.com> #
#########################################

#   DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# 
#Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
#Everyone is permitted to copy and distribute verbatim or modified
#copies of this license document, and changing it is allowed as long
#as the name is changed.
# 
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
# 0. You just DO WHAT THE FUCK YOU WANT TO.

import sys, os, datetime, shutil

###clear the terminal
os.system("clear")

###print title
print "\033[95mTinyText - A Python-based text file generator\033[0m"

###create a dir 
if not os.access(".TinyText", os.F_OK):
    os.mkdir(".TinyText")

filename = ".TinyText/file.txt"

###name file
print "\n\033[92mWhat would you like to name your file?\033[0m"
filename2 = raw_input()
print "\n"

###get the date and time
datetime = datetime.datetime.now()

###create the file
txtfile = file(filename,"wt")

###the title
title = raw_input("\033[92mHEAD -->\033[0m\n").strip()

###the entry
print "\n\n\033[92mTEXT -->\033[0m (Press CTRL-D to save and exit)"
entry = sys.stdin.read()

###build the file
print >> txtfile, "HEAD: ", title,"\n", "DATE: ", datetime, "\n", "\n", "TEXT: ", entry

###clear the terminal
os.system("clear")

###exit message
print "\033[92mSave successful!\033[0m\n"

###move file
src = filename 
dst = filename2
shutil.move(src, dst)

###exit
txtfile.close()
