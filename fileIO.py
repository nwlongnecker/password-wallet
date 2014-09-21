# Helper file for reading and writing to files

import os

# The file where we save the wallet data
WALLET_FILE = 'wallet'

# Checks whether the given file exists
# @return Returns true if the given file exists, false otherwise
def fileExists(path):
	return os.path.isfile(path)

# Writes the given text to the given file
# @param String text The text to write to the given file
def writeFile(path, text):
	f = open(path, 'w')
	try:
		f.write(text)
	finally:
		f.close()

# Reads the entire given file
# @return Returns the contents of the given file
def readFile(path):
	f = open(path, 'r')
	text = ""
	try: 
		text = f.read()
	finally:
		f.close()
	return text

# Creates a file with only wr permissions for this user
def createFile(path):
	os.open(path, os.O_WRONLY | os.O_CREAT, 0o600)
