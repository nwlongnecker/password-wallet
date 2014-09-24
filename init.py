# The init command for intializing the wallet or reinitializing the wallet

import coreRoutines as cr
import fileIO
import uiHelper
import openSSL

# Check whether the wallet has already been initialized
if cr.existsWallet():
	print('\nWallet already initialized\n')
	if uiHelper.askReset():
		# Get old password key
		key = openSSL.hash(uiHelper.getPassword(), '-binary')
		# Open the wallet to check that the old password is valid
		cr.openWallet(key)
		# Create a new wallet
		cr.newWallet()
else:
	cr.newWallet()
