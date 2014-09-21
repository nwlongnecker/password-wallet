# Helper file for reading and writing to files

import os.path

# The file where we save the wallet data
WALLET_FILE = 'wallet'

# Checks whether the wallet file exists
# @return Returns true if the wallet file exists, false otherwise
def fileExists():
	return os.path.isfile(WALLET_FILE)

# Writes the given text to the wallet file
# @param String text The text to write to the wallet file
def writeFile(text):
	f = open(WALLET_FILE, 'w')
	f.write(text)

# Reads the entire wallet file
# @return Returns the contents of the wallet file
def readFile():
	f = open(WALLET_FILE, 'r')
	return f.read()
