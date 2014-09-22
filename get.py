# The get command for retrieving passwords from the password wallet

import coreRoutines as cr
import uiHelper
import openSSL
import re
import fileIO
import sys

# Check to make sure the wallet has been initialized
if not fileIO.fileExists(fileIO.WALLET_FILE):
	sys.exit('Wallet not initialized')
# Get password key
key = openSSL.hash(uiHelper.getPassword(), '-binary')
# Open the wallet using the key
wallet = cr.openWallet(key)
# Prompt the user for the site to retrieve
site = uiHelper.getSite()
# Search the wallet for the site,password key-value pair using a regular expression
# The regular expression looks like this: ^(site),(password)$
found = re.search(r'^(' + site + '),(.*)$', wallet, re.M)
if found:
	# Copy the password to the system clipboard
	print found.group(2)
	uiHelper.addToClipboard(found.group(2))
	print('Password copied to clipboard')
else:
	print('Could not find ' + site + ' in your wallet')
