# Helper file for commonly used routines in the password wallet program

import fileIO
import uiHelper
import openSSL
import sys

# Make sure python2.7 is being used
if sys.version_info < (2, 7) or sys.version_info >= (2, 8):
	sys.exit('\nNot running python 2.7\n')

# The first line of the password wallet
# Used to check if the decryption was successful
FIRST_LINE = 'Password Wallet:'
WALLET_FILE = 'wallet'

# Checks that the wallet exists
# @return true if the wallet exists, false otherwise
def existsWallet():
	return fileIO.fileExists(WALLET_FILE)

# Attempts to use the given key to open the password wallet
# If the key is correct, will return the contents of the
# wallet in plaintext. Otherwise, will exit the program
# @param String key The key to use when decrypting the wallet
# @return The contents of the wallet in plaintext
def openWallet(key):
	encrypted = fileIO.readFile(WALLET_FILE)
	plaintext = "nothing"
	try:
		plaintext = openSSL.decrypt(key, encrypted)
	except:
		pass
	if plaintext.splitlines()[0] != FIRST_LINE:
		sys.exit('\nIncorrect Password\n')
	return plaintext

# Encrypts the password wallet with the given key and
# writes it to disk
# @param String key The key to use when encrypting the wallet
# @param String plaintext The plaintext contents of the password wallet
def closeWallet(key, plaintext):
	encrypted = openSSL.encrypt(key, plaintext)
	fileIO.writeFile(WALLET_FILE, encrypted)

# Creates a new wallet. Will overwrite the previous wallet.
def newWallet():
	password = uiHelper.getPassword('New Password:')
	confirmPassword = uiHelper.getPassword('Confirm New Password:')
	if password == confirmPassword:
		key = openSSL.hash(password, '-binary')
		closeWallet(key, FIRST_LINE + '\n')
		print('Wallet created')
	else:
		sys.exit('\nPasswords do not match\n')
