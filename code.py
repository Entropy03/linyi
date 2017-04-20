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
codeimg = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&%s' % random.random()
ssl._create_default_https_context = ssl._create_unverified_context

def get(url):
    try:
        request = urllib2.Request(url=url)
        # req.add_header('User-Agent', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0')
        request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=utf-8")
        request.add_header('X-Requested-With', 'xmlHttpRequest')
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
        request.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
        request.add_header('Accept', '*/*')
        result = urllib2.urlopen(request).read()
        assert isinstance(result, object)
        return result
    except httplib.error as e:
        print e
        pass
    except urllib2.URLError as e:
        print e
        pass
    except urllib2.HTTPBasicAuthHandler, urllib2.HTTPError:
        print 'error'
        pass

def getImg():
    result = get(codeimg)
    try:
        if open('./tkcode', 'wb').write(result) :
            import os
            os.system("oeg ./tkcode &")
        else:
            return False
    except OSError as e:
        print e
        pass

if __name__ == "__main__":
	getImg()
