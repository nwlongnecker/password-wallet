# Helper file for reading and writing to files

import os
import stat

# The default permissions of files
PERMISSIONS = stat.S_IWUSR | stat.S_IRUSR

# The file where we save the wallet data
WALLET_FILE = 'wallet'

# Checks whether the given file exists
# @return Returns true if the given file exists, false otherwise
def fileExists(path):
	return os.path.isfile(path)

# Writes the given text to the given file
# @param String text The text to write to the given file
def writeFile(path, text):
	with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, PERMISSIONS), 'w') as file: 
		file.write(text)

# Reads the entire given file
# @return Returns the contents of the given file
def readFile(path):
	if fileExists(path):
                with os.fdopen(os.open(path, os.O_RDONLY, PERMISSIONS), 'r') as file:
                        return file.read()
        else:
                raise Exception("readFile("+path+"): Could not find file")

# Removes a file
def removeFile(path):
	if fileExists(path):
		os.remove(path)
