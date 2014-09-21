import coreRoutines as cr
import openSSL
import uiHelper

key = openSSL.hash(uiHelper.getPassword())
wallet = cr.openWallet(key)
site = uiHelper.getSite()
newPassword = openSSL.generatePassword()
wallet = wallet + site + ',' + newPassword + '\n'
cr.closeWallet(key, wallet)
uiHelper.addToClipboard(newPassword)
