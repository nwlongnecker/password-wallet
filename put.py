# The put command for adding new sites to the password wallet

import coreRoutines as cr
import uiHelper
import openSSL
import fileIO
import sys

# Check to make sure the wallet has been initialized
if not cr.existsWallet():
	sys.exit('\nWallet not initialized\n')
# Prompts the user for the master password and hashes it into the encryption key
key = openSSL.hash(uiHelper.getPassword(), '-binary')
# Open the wallet using the key
wallet = cr.openWallet(key)
# Prompt the user for the site to add
site = uiHelper.getSite()
# Generate a new password for this site
newPassword = openSSL.generatePassword()
# Append the password to the wallet
wallet = wallet + site + ',' + newPassword
# Write the change to the wallet using the key
cr.closeWallet(key, wallet)
# Copy the new password to the clipboard
uiHelper.addToClipboard(newPassword)
