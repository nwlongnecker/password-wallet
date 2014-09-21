import getpass
from tkinter import Tk

def getPassword(prompt = 'Password: '):
	return getpass.getpass(prompt)

def getSite():
	return input('Site: ')

def addToClipboard(text):
	tk = Tk()
	tk.clipboard_clear()
	tk.clipboard_append(text)
	tk.destroy()
