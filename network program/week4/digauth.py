import resource
import requests
from requests.auth import HTTPBasicAuth

url = 'http://httpbin.org/digest-auth/auth/user/pass'

resource = requests.get(url, auth=HTTPBasicAuth('user','pass'))
print('Response.status_code : '+ str(resource.status_code))
if resource.status_code == 200:
    print('Login successful : '+ str(resource.json()))