# This program will automate the set up of my web dev creating/editing environment
# The program will also add an entry to a document as a way of clocking in and 
# tracking my hours worked with the option to specify if I'm working on a 
# certain project.

# usage in Terminal: cd to proper dir / python onescript.py

import os
import subprocess
import datetime

currentDT = datetime.datetime.now()

# placeholder until I make it work
project_info = ['Holy Spirit','this is a comment']



def main():
	intro()
	update_log(project_info)
	#os.system("open newfile.txt")

def check_input():
	# implement code to verify arg count
	# notify the user if they did not meet proper usage guidelines
	print("Hello World")

def update_log(project_info): 
# project_info is a set with the project name and the appropriate comment
	# open log.txt or create if not yet created
	f=open("newfile.txt", "a+")
	# using zfill to make sure there are always 2 numbers, for consistency
	today_date = str(currentDT.month).zfill(2) + "/" + str(currentDT.day).zfill(2) + "/" + str(currentDT.year)
	today_time = str(currentDT.hour).zfill(2) + ":" + (str(currentDT.minute)).zfill(2) 

	# append the date, time, project name, and comment to log
	f.write(today_date)
	f.write(" ")
	f.write(today_time)
	f.write(" Project: ")
	f.write(project_info[0])
	f.write(" | Comment: ")
	f.write(project_info[1])
	f.write("\n")
	f.close()

def intro():
	print("Hello World")

main()

