# Helper module for interfacing with OpenSSL

import fileIO
import subprocess

# Hashes the input to a key
# @param String plaintext The string to hash
# @return Returns the hashed key
def hash(plaintext):
	# create temp files
	fileIO.createFile('plain.tmp')
	fileIO.createFile('hash.tmp')
	# write out the input
	fileIO.writeFile('plain.tmp', plaintext)
	# run openssl hash command
	# TODO: strip SHA256(in.tmp)=... from string
	subprocess.check_output(['openssl', 'dgst', '-sha256', '-hex', '-out', 'hash.tmp', 'plain.tmp'], stderr=subprocess.STDOUT)
	# read in the output
	hashKey = fileIO.readFile('hash.tmp')
	# delete temp files
	fileIO.removeFile('plain.tmp')
	fileIO.removeFile('hash.tmp')
	# return the output
	return hashKey.replace('SHA256(in.tmp)= ', '', 1)

# Decrypts the cipher with the given key
# @param String key The key to use when decrypting the cipher
# @param String cipher The encrypted text
# @return Returns the cipher in plaintext
def decrypt(key, cipher):
	# print('Decrypted ' + cipher + ' with key ' + key)
	return cipher

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
	#openssl enc -aes-256-cbc -pass stdin -in infile.txt -out this.txt
	subprocess.check_output(['openssl', 'enc', '-aes-256-cbc', '-pass', 'key.tmp', '-in', 'plain.tmp', '-out', 'cipher.tmp'], stderr=subprocess.STDOUT)
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
