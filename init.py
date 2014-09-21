# The init command for intializing the wallet or reinitializing the wallet

import coreRoutines as cr
import fileIO
import uiHelper
import openSSL

# Check whether the wallet has already been initialized
if fileIO.fileExists():
	print('Wallet already initialized')
	if input('Do you want to reset? (y/n) ') == 'y':
		# Require the old password to reset the wallet
		oldKey = openSSL.hash(uiHelper.getPassword('Old Password:'))
		# Open the wallet to check that the old password is valid
		cr.openWallet(oldKey)
		# Create a new wallet
		cr.newWallet()
else:
	cr.newWallet()
