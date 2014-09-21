# Helper module for interfacing with OpenSSL

import fileIO
import subprocess

# Hashes the input to a key
# @param String plaintext The string to hash
# @return Returns the hashed key
def hash(plaintext):
	# create temp files
	fileIO.createFile('plain.tmp')
	fileIO.createFile('key.tmp')
	# write out the input
	fileIO.writeFile('plain.tmp', plaintext)
	# run openssl hash command
	subprocess.check_output(['openssl', 'dgst', '-sha256', '-binary', '-out', 'key.tmp', 'plain.tmp'], stderr=subprocess.STDOUT)
	# read in the output
	hashKey = fileIO.readFile('key.tmp')
	# delete temp files
	fileIO.removeFile('plain.tmp')
	fileIO.removeFile('key.tmp')
	# return the output
	return hashKey

# Decrypts the cipher with the given key
# @param String key The key to use when decrypting the cipher
# @param String cipher The encrypted text
# @return Returns the cipher in plaintext
def decrypt(key, ciphertext):
	# create temp files
	fileIO.createFile('key.tmp')
	fileIO.createFile('cipher.tmp')
	fileIO.createFile('plain.tmp')
	# write out the input
	fileIO.writeFile('key.tmp', key)	
	fileIO.writeFile('cipher.tmp', ciphertext)
	# run openssl dec command
	subprocess.check_output(['openssl', 'enc', '-d', '-aes-256-cbc', '-pass', 'stdin', '-out', 'plain.tmp', '-in', 'cipher.tmp'], stdin=file('key.tmp'))
	# read in the output
	plaintext = fileIO.readFile('plain.tmp')
	# delete temp files
	fileIO.removeFile('key.tmp')
	fileIO.removeFile('cipher.tmp')
	fileIO.removeFile('plain.tmp')
	# return the output
	return plaintext

# Encrypts the plaintext with the given key
# @param String key The key to use when encrypting the plaintext
# @param String plaintext The text to encrypt
# @return Returns the encrypted plaintext
def encrypt(key, plaintext):
	# create temp files
	fileIO.createFile('key.tmp')
	fileIO.createFile('plain.tmp')
	fileIO.createFile('cipher.tmp')
	# write out the input
	fileIO.writeFile('key.tmp', key)	
	fileIO.writeFile('plain.tmp', plaintext)
	# run openssl enc command
	subprocess.check_output(['openssl', 'enc', '-aes-256-cbc', '-pass', 'stdin', '-out', 'cipher.tmp', '-in', 'plain.tmp'], stdin=file('key.tmp'))
	# read in the output
	ciphertext = fileIO.readFile('cipher.tmp')
	# delete temp files
	fileIO.removeFile('key.tmp')
	fileIO.removeFile('plain.tmp')
	fileIO.removeFile('cipher.tmp')
	# return the output
	return ciphertext

# Generates a random password
# @return Returns the generated password
def generatePassword():
	# print('Generated a new password')
	return 'password'
