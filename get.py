import coreRoutines as cr
import uiHelper
import openSSL
import re

key = openSSL.hash(uiHelper.getPassword())
wallet = cr.openWallet(key)
site = uiHelper.getSite()
found = re.search(r'^(' + site + '),(.*)$', wallet, re.M)
if found:
	uiHelper.addToClipboard(found.group(2))
	print('Password copied to clipboard')
else:
	print('Could not find ' + site + ' in your wallet')
