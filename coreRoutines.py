import fileIO
import uiHelper
import openSSL
import sys

FIRST_LINE = 'Password Wallet:'

def openWallet(key):
	encrypted = fileIO.readFile()
	plaintext = openSSL.decrypt(key, encrypted)
	if plaintext.splitlines()[0] != FIRST_LINE:
		sys.exit('Incorrect Password')
	return plaintext

def closeWallet(key, plaintext):
	encrypted = openSSL.encrypt(key, plaintext)
	fileIO.writeFile(encrypted)

def newWallet():
	password = uiHelper.getPassword('New Password:')
	confirmPassword = uiHelper.getPassword('Confirm New Password:')
	if password == confirmPassword:
		key = openSSL.hash(password)
		closeWallet(key, FIRST_LINE + '\n')
		print('Wallet created')
	else:
		print('Passwords do not match')