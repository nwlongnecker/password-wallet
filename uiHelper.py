# Helper module for interfacing with the user

import getpass
import subprocess

# Prompts the user for a password without echoing raw_input
# @param String prompt The prompt to display
# @return Returns the password the user raw_input
def getPassword(prompt = 'Password: '):
	return getpass.getpass(prompt)

# Prompts the user for a website name
# @return Returns the site the user raw_input
def getSite():
	return raw_input('Site: ')

# Asks the user if they want to reset their wallet or not
# @return true if they do; false otherwise
def askReset():
	return raw_input("Do you want to reset? (y/n)") == 'y'

# Copies the given text to the system clipboard
# @param String text The text to paste to the system clipboard
def addToClipboard(text):
	try:
		p1 = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
		p2 = subprocess.Popen(["xclip"], stdin=p1.stdout, stdout=subprocess.PIPE)
		p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
		p2.communicate()[0]
		print "password copied to clipboard"
	except:
		print ""
		print "Unable to copy password to clipboard using xclip;"
		print "Possible issues..."
		print "\txclip is not installed (try sudo apt-get xclip)"
		print "\tyou do not have access to the clipboard"
		print "\tyou are ssh'd in to a unix terminal"
		print ""
		print "Password= ", text
