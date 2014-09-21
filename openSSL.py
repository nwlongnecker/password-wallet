# Helper module for interfacing with OpenSSL

import fileIO
import subprocess

INPUT_FILE = "in.tmp"
OUTPUT_FILE = "out.tmp"

# Hashes the input to a key
# @param String plaintext The string to hash
# @return Returns the hashed key
def hash(plaintext):
	# create temp files
	fileIO.createFile(INPUT_FILE)
	fileIO.createFile(OUTPUT_FILE)
	# write out the input
	fileIO.writeFile(INPUT_FILE, plaintext)
	# run openssl hash command
	# TODO: strip SHA256(in.tmp)=... from string
	subprocess.check_output(['openssl', 'dgst', '-sha256', '-hex', '-out', OUTPUT_FILE, INPUT_FILE], stderr=subprocess.STDOUT)
	# read in the output
	hashKey = fileIO.readFile(OUTPUT_FILE)
	# delete temp files
	fileIO.removeFile(INPUT_FILE)
	fileIO.removeFile(OUTPUT_FILE)
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
	# print('Encrypted ' + plaintext + ' with key ' + key)
	return plaintext

# Generates a random password
# @return Returns the generated password
def generatePassword():
	# print('Generated a new password')
	return 'password'
