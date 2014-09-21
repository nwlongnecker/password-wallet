import os.path
WALLET_FILE = 'wallet'

def fileExists():
	return os.path.isfile(WALLET_FILE)

def writeFile(text):
	f = open(WALLET_FILE, 'w')
	f.write(text)

def readFile():
	f = open(WALLET_FILE, 'r')
	return f.read()