# Helper module for interfacing with the user

import getpass
from Tkinter import Tk

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
	tk = Tk()
	tk.clipboard_clear()
	tk.clipboard_append(text)
	tk.destroy()
