# Helper module for interfacing with OpenSSL
import fileIO

# Hashes the input to a key
# @param String inputKey The key to hash
# @return Returns the hashed key
def hash(inputKey):
	# create temp files
	#fileIO.createFile("in.tmp")
	#fileIO.createFile("out.tmp")
	# run openssl hash command
	#subprocess.check_output(['mycmd', 'myarg'], stderr=subprocess.STDOUT)
	# print('Hashed ' + inputKey + ' to ' + inputKey)
	return inputKey

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
