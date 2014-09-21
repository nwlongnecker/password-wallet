import getpass
from tkinter import Tk

def getPassword():
	return getpass.getpass()

def addToClipboard(text):
	tk = Tk()
	tk.clipboard_clear()
	tk.clipboard_append(text)
	tk.destroy()
