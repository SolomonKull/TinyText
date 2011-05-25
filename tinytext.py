#!/usr/bin/env python

#########################################
### TinyText 1.0 ########################
### Copyright (C) 2011 ##################
### SolomonKull <solomonkull@gmail.com>##
#########################################

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
print "\n\n\033[92mBLOG -->\033[0m (Press CTRL-D to save and exit)"
entry = sys.stdin.read()

###build the file
print >> txtfile, "HEAD: ", title,"\n", "DATE: ", datetime, "\n", "\n", "BLOG: ", entry

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
