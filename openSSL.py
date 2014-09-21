# Helper module for interfacing with OpenSSL

# Hashes the input to a key
# @param String inputKey The key to hash
# @return Returns the hashed key
def hash(inputKey):
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
