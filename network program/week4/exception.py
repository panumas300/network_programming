import imp
from urllib import response


import urllib.error
from urllib.request import urlopen
try:
    response = urlopen('http://www.youtube.com')
    print(response.status)
except urllib.error.HTTPError as e:
    print('Exception', e)
    print('status', e.code)
    print('reason', e.reason)
    print('url', e.url)