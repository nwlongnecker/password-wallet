import coreRoutines as cr
import uiHelper
import openSSL
import re

key = openSSL.hash(uiHelper.getPassword())
wallet = cr.openWallet(key)
site = uiHelper.getSite()
found = re.search(r'^(' + site + '),(.*)$', wallet, re.M)
if found:
	wallet = wallet.replace(found.group() + '\n', '')
	cr.closeWallet(key, wallet)
	print(site + ' removed from wallet')
else:
	print('Could not find ' + site + ' in your wallet')
