# Helper module for interfacing with the user

import getpass
from tkinter import Tk

# Prompts the user for a password without echoing input
# @param String prompt The prompt to display
# @return Returns the password the user input
def getPassword(prompt = 'Password: '):
	return getpass.getpass(prompt)

# Prompts the user for a website name
# @return Returns the site the user input
def getSite():
	return input('Site: ')

# Copies the given text to the system clipboard
# @param String text The text to paste to the system clipboard
def addToClipboard(text):
	tk = Tk()
	tk.clipboard_clear()
	tk.clipboard_append(text)
	tk.destroy()
