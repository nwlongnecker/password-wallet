# The del command for removing sites from the password wallet

import coreRoutines as cr
import uiHelper
import openSSL
import re
import fileIO
import sys

# Check to make sure the wallet has been initialized
if not fileIO.fileExists():
	sys.exit('Wallet not initialized')
# Prompts the user for the master password and hashes it into the encryption key
key = openSSL.hash(uiHelper.getPassword())
# Open the wallet using the key
wallet = cr.openWallet(key)
# Prompt the user for the site to delete
site = uiHelper.getSite()
# Search the wallet for the site,password key-value pair using a regular expression
# The regular expression looks like this: ^(site),(password)$
found = re.search(r'^(' + site + '),(.*)$', wallet, re.M)
if found:
	# Replace the line with an empty string
	wallet = wallet.replace(found.group() + '\n', '')
	# Write the changes to the wallet using the key
	cr.closeWallet(key, wallet)
	print(site + ' removed from wallet')
else:
	print('Could not find ' + site + ' in your wallet')
