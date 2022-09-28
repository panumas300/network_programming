from cgitb import reset
from http.client import responses
import imp
import requests

from requests.auth import HTTPBasicAuth

requests.get('https://api.github.com/uesr', auth=HTTPBasicAuth('user','password'))

responses = requests.get('https://api.github.com/user', auth=('user','password'))

print('Response.status_code : '+ str(responses.status_code))
if responses.status_code == 200:
    print('Login successfully : '+ responses.text)