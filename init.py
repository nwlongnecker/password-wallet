import coreRoutines as cr
import fileIO
import uiHelper
import openSSL

if fileIO.fileExists():
	print('Wallet already initialized')
	if input('Do you want to reset? (y/n) ') == 'y':
		oldKey = openSSL.hash(uiHelper.getPassword('Old Password:'))
		cr.openWallet(oldKey)
		cr.newWallet()
else:
	cr.newWallet()