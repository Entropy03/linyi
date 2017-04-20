import ssl
import sys
import urllib2
import random
import httplib
import json
from cookielib import LWPCookieJar
import urllib
import re
import getpass

class lgoin :

	def __init__(self) :
		self.logindata = {}
		self.username ='china199123@163.com'
		self.password ='ZAQjay12306'
		self.randcode = ''
	    #在http交互中即时更新cookie
        self.cookiejar = LWPCookieJar()
        cookiesupport = urllib2.HTTPCookieProcessor(self.cookiejar)
        opener = urllib2.build_opener(cookiesupport, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def getrandcode(self):