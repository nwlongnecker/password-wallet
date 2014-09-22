# Helper module for interfacing with OpenSSL

import fileIO
import subprocess
from datetime import datetime

# Hashes the input to a key
# @param String plaintext The string to hash
# @return Returns the hashed key
def hash(plaintext, outputType):
	hashKey = "nothing"
	try:
		# create temp files
		fileIO.createFile('plain.tmp')
		fileIO.createFile('key.tmp')
		# write out the input
		fileIO.writeFile('plain.tmp', plaintext)
		# run openssl hash command
		subprocess.check_output(['openssl', 'dgst', '-sha256', outputType, '-out', 'key.tmp', 'plain.tmp'])
		# read in the output
		hashKey = fileIO.readFile('key.tmp')
	finally:
		# delete temp files
		fileIO.removeFile('plain.tmp')
		fileIO.removeFile('key.tmp')
		# return the output
		return hashKey.replace('SHA256(plain.tmp)= ', '', 1)

# Decrypts the cipher with the given key
# @param String key The key to use when decrypting the cipher
# @param String cipher The encrypted text
# @return Returns the cipher in plaintext
def decrypt(key, ciphertext):
	plaintext = "nothing"
	try:
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
	finally:
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
	ciphertext = "nothing"
	try:
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
	finally:
		# delete temp files
		fileIO.removeFile('key.tmp')
		fileIO.removeFile('plain.tmp')
		fileIO.removeFile('cipher.tmp')
		# return the output
		return ciphertext

# Generates a random password
# @return Returns the generated password
def generatePassword():
	# get the current time
	time = datetime.now().time()
	# get a random number
	rand = subprocess.check_output(['openssl', 'rand', '-hex', '16'])
	# return the hash of the current time and random nonce value
	return hash(str(time)+str(rand), '-hex')
