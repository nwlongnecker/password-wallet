import fileIO
import openSSL
import AuthenticationError as e

def openWallet(key):
	encrypted = fileIO.readFile()
	plaintext = openSSL.decrypt(key, encrypted)
	if plaintext.splitlines()[0] != 'Password Wallet:':
		raise e.AuthenticationError('Incorrect Password')
	return plaintext

def closeWallet(key, plaintext):
	encrypted = openSSL.encrypt(key, plaintext)
	fileIO.writeFile(encrypted)
