import coreRoutines as cr
import openSSL
import uiHelper

key = openSSL.hash(uiHelper.getPassword())
cr.openWallet(key)
